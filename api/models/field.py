from models.base import Base
from peewee import CharField, UUIDField


class Field(Base):
    icao = CharField(max_length=4, primary_key=True)
    name = CharField()

    @classmethod
    def get_all_fields(cls):
        return cls.parse_multiple_results(
            cls.select()
            .order_by(cls.icao)
        )

    @classmethod
    def get_by_icao(cls, icao: str):
        return cls.get_or_none(cls.icao == icao)

    def to_dict(self):
        return {
            'icao': self.icao,
            'name': self.name,
        }
