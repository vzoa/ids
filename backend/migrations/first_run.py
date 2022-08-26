from models.atis import Atis
from models.field import Field
from storage.db import db

tables = [Atis, Field]

for table in tables:
    if db.table_exists(table):
        db.drop_tables([table])
        db.create_tables([table])
