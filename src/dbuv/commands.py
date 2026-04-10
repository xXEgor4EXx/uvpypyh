import time

import click # type: ignore
from .dbmodels import User, Todo
from rich.live import Live

@click.command()
@click.pass_obj
def create_tables(db):
    """Инициализация БД"""
    db.create_tables([User, Todo])


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

@click.command()
@click.argument("task")
def add_task(task):
    """Добавить задание в Todo"""
    task1: Todo = Todo.create(task=task)
    print(task1.task)

@click.command()
def get_tasks():
    """Получить все задачи и Todo"""
    for task in Todo.select():
        status = "Done" if task.is_done else "Not_Done"
        print(f"[{status}] {task.task}")

@click.command()
@click.argument("task")
def delete_task(task):
    """Удалить задачу по имени"""
    tasks = list(Todo.select())
    if not tasks:
        print("задач нет")
        return
    while True:
        print("\n Текущие задачи:")
        for i, task in enumerate(tasks, 1):
            status = "done" if task.is_done else "not done"
            print(f"{i}. [{status}] {task.task}")
        choice = click.prompt("Номер задачи для удаления (0 - выход)", type=int)
        if choice == 0:
            break
        elif 1 <= choice <= len(tasks):
            task = tasks[choice - 1]
            task.delete_instance()
            print(f"Удалено: {task.task}")  
            with Live(Todo(), refresh_per_second=4) as live:
                for _ in range(40):
                    time.sleep(0.4)
                    live.update(Todo())
        else:
            print("Неверный номер")

@click.command()
def mark_done():
    """Отметить выполненной (интерактивно)"""
    while True:
        tasks = list(Todo.select().where(Todo.is_done == False))
        if not tasks:
            print("Невыполненных задач нет")
            break
    
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task.task}")
    
        choice = click.prompt("Номер задачи (0 - для выхода)", type=int)
        if choice == 0:
            break
        elif 1 <= choice <= len(tasks):
            task = tasks[choice - 1]
            task.is_done = True
            task.save()
            print(f"Выполнено: {task.task}")
        else:
            print("Неверный номер")

@click.command()
def mark_undone():
    """Снять выполнение (интерактивно)"""
    while True:

        tasks = list(Todo.select().where(Todo.is_done == True))
        if not tasks:
            print("Выполненных задач нет")
            break
    
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task.task}")
    
        choice = click.prompt("Номер задачи (0 - для выхода)", type=int)
        if choice == 0:
            break
        elif 1 <= choice <= len(tasks):
            task = tasks[choice - 1]
            task.is_done = False
            task.save()
            print(f"Не выполнено: {task.task}")
        else:
            print("Неверный номер")