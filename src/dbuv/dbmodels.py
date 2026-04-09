from peewee import SqliteDatabase, Model, CharField

#объект БД без привязки к пути (инициализируем потом)
db = SqliteDatabase(None)

class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    name = CharField()