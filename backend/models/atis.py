from peewee import ForeignKeyField, UUIDField, CharField

from models.base import Base
from models.field import Field


class Atis(Base):
    id = UUIDField(primary_key=True)
    field = ForeignKeyField(Field, backref='atises')
    code = CharField()
