from peewee import SqliteDatabase, Model, CharField, BooleanField # type: ignore

#объект БД без привязки к пути (инициализируем потом)
db = SqliteDatabase(None)

class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    name = CharField()

class Todo(BaseModel):
    task = CharField()
    is_done = BooleanField(default=False)
