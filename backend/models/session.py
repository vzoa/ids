from models.base import Base
from peewee import DateTimeField, UUIDField


class Session(Base):
    session = UUIDField(primary_key=True)
    created = DateTimeField()
    expires = DateTimeField()
