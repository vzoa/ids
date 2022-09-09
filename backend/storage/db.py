import os

from peewee import MySQLDatabase, SqliteDatabase

connection_type = os.getenv("DATABASE_TYPE")

if connection_type is not None and connection_type == "MYSQL":
    db = MySQLDatabase(os.getenv("MYSQL_DB_NAME"),
                       host=os.getenv("MYSQL_DB_HOST"),
                       port=os.getenv("MYSQL_DB_PORT"),
                       user=os.getenv("MYSQL_DB_USER"),
                       password=os.getenv("MYSQL_DB_PASSWORD"))
else:
    # it's guaranteed to be sqlite in this case as we don't support anything else right now
    # @TODO - throw a more sane error in the event some env vars are missing
    relative_path = os.getenv("SQLITE_DB_RELATIVE_PATH") or "/../var/database.db"
    db = SqliteDatabase(os.path.dirname(__file__) + relative_path)
