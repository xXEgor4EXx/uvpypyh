import click # type: ignore
from peewee import * # type: ignore
from .dbmodels import db
from .commands import create_tables, add_user, get_users,get_users_by_name, add_task, get_tasks, delete_task, mark_done, mark_undone

def main() -> None:
    print("Hello from uv-1!")

@click.group()
@click.option('--db-path', default='orm2.db', help='Путь к базе данных')
@click.pass_context
def cli(ctx, db_path):
    ''' Подключение к БД'''
    print('closed ?',db.is_closed())
    db.init(db_path)
    db.connect()
    print('closed ?',db.is_closed())

    ctx.obj = db # Сохраняем подключение в контекст
    ctx.call_on_close(lambda: db.close()) # Закрываем подключение при выходе

# Регистрируем команды
cli.add_command(create_tables)
cli.add_command(add_user)
cli.add_command(get_users)
cli.add_command(get_users_by_name)
cli.add_command(add_task)
cli.add_command(get_tasks)
cli.add_command(delete_task)
cli.add_command(mark_done)
cli.add_command(mark_undone)

