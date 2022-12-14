from models.base import Base
from peewee import DateTimeField, UUIDField


class Session(Base):
    """
    Session model

    Attributes:
        id (UUIDField): Session ID
        created_at (DateTimeField): Session creation date
        updated_at (DateTimeField): Session update date
        user_id (UUIDField): User ID
    """
    id = UUIDField(primary_key=True)
    created_at = DateTimeField()
    updated_at = DateTimeField()
    user_id = UUIDField()

    class Meta:
        table_name = 'sessions'
