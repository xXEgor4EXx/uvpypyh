import click
from .dbmodels import User


@click.command()
@click.pass_obj
def create_tables(db):
    """Инициализация БД"""
    db.create_tables([User])


@click.command()
@click.argument("username")
def add_user(username):
    """Добавить пользователя"""
    user1: User = User.create(name=username)
    print(user1.name)
    # user1 = User(name='Иванов') 2-й вар-т
    # user1.save()


@click.command()
def get_users():
    """Получить список всех пользователей"""
    for user in User.select():
        print(user.name)


@click.command()
@click.argument("username")
def get_users_by_name(username):
    """Получить пользователей по условию"""
    for user in User.select().where(User.name == username):
        print(user.name)
