#!/usr/bin/env python
import json
import os.path

from ids.models.atis import Atis
from ids.models.field import Field
from ids.storage.db import db


def find_all_models():
    pass


def reset():
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
