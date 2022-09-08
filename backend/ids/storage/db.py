import os

from peewee import SqliteDatabase

# TODO logic to setup the database stuff based on configuration
db = SqliteDatabase(os.path.dirname(__file__) + '/../../var/database.db')
