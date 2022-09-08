#!/usr/bin/env python
import importlib
import inspect
import json
import os.path

from ids.models.atis import Atis
from ids.models.field import Field
from ids.storage.db import db


def find_all_models():
    for file in os.scandir(os.path.dirname(__file__) + "/../models/"):
        for name, cls in inspect.getmembers(importlib.import_module(f"models.{file}"), inspect.isclass):
            print(f"found class {cls}")


def reset():
    find_all_models()
    tables = [Atis, Field]
    for table in tables:
        if db.table_exists(table):
            db.drop_tables([table])
            db.create_tables([table])

    fixtures_path = os.path.dirname(__file__) + "/fixtures"

    with open(f"{fixtures_path}/fields.json") as fields_fixtures:
        for field in json.load(fields_fixtures):
            Field.create(**field).save()


reset()
