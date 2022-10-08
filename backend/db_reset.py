#!/usr/bin/python
# This file is built so that you can quickly recreate a local database.
# WARNING: It will destroy any database it touches.
import getopt
import importlib
import inspect
import json
import os.path
import sys
from typing import List, Type

import models.base
from storage.db import db


file_dir = os.path.dirname(os.path.realpath(__file__))


def find_all_models() -> List[Type[models.base.Base]]:
    classes = set()
    for file in os.scandir(f"{file_dir}/models/"):
        # only get python files and ignore __init__.py and base.py
        if file.name[-3:] == ".py" and file.name not in ["__init__.py", "base.py:"]:
            for name, cls in inspect.getmembers(importlib.import_module(f"models.{file.name[:-3]}"), inspect.isclass):
                if issubclass(cls, models.base.Base) and cls != models.base.Base:
                    classes.add(cls)

    return list(classes)


def load_fixtures_for_table(table):
    print("Loading fixtures because '-l' was provided")
    fixture_path = file_dir + f"/migrations/fixtures/{str(table.__name__).lower()}.json"
    if os.path.exists(fixture_path):
        print(f"Populating fixtures for {table}")
        with open(f"{fixture_path}") as fixture_data:
            for entry in json.load(fixture_data):
                table.create(**entry).save()


def reset(load_fixtures=False):
    tables = find_all_models()
    print(f"Found tables to prep for {tables}")
    for table in tables:
        if db.table_exists(table):
            print(f"Dropping {table}")
            db.drop_tables([table])
        print(f"Creating {table}")
        db.create_tables([table])

        if load_fixtures:
            load_fixtures_for_table(table)


def main(argv):
    try:
        opts, args = getopt.getopt(argv, "l")
    except getopt.GetoptError:
        print("db_reset.py")
        print("  -l    Loads all available fixtures.")
        sys.exit(2)

    reset(("-l", "") in opts)


if __name__ == "__main__":
    main(sys.argv[1:])
