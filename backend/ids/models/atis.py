from peewee import ForeignKeyField, UUIDField, CharField

from ids.models.base import Base
from ids.models.field import Field


class Atis(Base):
    id = UUIDField(primary_key=True)
    field = ForeignKeyField(Field, backref='atises')
    code = CharField()
