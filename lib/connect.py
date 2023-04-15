from peewee import *

db = PostgresqlDatabase(
    'Bookmakrs',
    user='postgres',
    password='',
    host='localhost',
    port='5432'
    )
db.connect()

class BaseModel(Model):
    class Meta: 
        dabase = db

class Bookmark(BaseModel):
    title = CharField()
    url = CharField()
    description = CharField()

db.create_tables([Bookmark])

