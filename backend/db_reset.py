import importlib
import inspect
import json
import os.path
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


def reset():
    tables = find_all_models()
    print(f"found tables to prep for {tables}")
    for table in tables:
        if db.table_exists(table):
            print(f"Resetting table {table}")
            db.drop_tables([table])
            db.create_tables([table])

        fixture_path = file_dir + f"/migrations/fixtures/{str(table.__name__).lower()}.json"
        if os.path.exists(fixture_path):
            print(f"Populating fixtures for {table}")
            with open(f"{fixture_path}") as fixture_data:
                for entry in json.load(fixture_data):
                    table.create(**entry).save()


reset()
