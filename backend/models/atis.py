from peewee import ForeignKeyField, UUIDField, CharField, TextField, TimestampField, BooleanField

from models.base import Base
from models.field import Field


class Atis(Base):
    id = UUIDField(primary_key=True)
    field = ForeignKeyField(Field, backref='atises')
    code = CharField()
    conditions = TextField()
    notams = TextField()
    timestamp = TimestampField()
    created = TimestampField()
    active = BooleanField()

    @classmethod
    def get_active_atis(cls):
        return cls.parse_multiple_results(
            cls.select()
            .where(cls.active == True)  # noqa E712 - as peewee only works with this as an equality operator
        )

    def to_dict(self):
        return {
            'id': self.id,
            'field': self.field.icao,
            'code': self.code,
            'conditions': self.conditions,
            'notams': self.notams,
            'timestamp': self.timestamp,
            'created': self.created
        }
