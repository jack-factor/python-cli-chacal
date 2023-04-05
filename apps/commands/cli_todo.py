from apps.resources.rs_todo_list import CliTodoList
from rich.table import Table
from rich.console import Console
import click


@click.group()
def cli_td():
    pass


@cli_td.command()
def init():
    CliTodoList.init()


@cli_td.command()
@click.option('--title', '-t', prompt='New todo list', help='New todo list name.')
def create(title):
    CliTodoList.create(title)


@cli_td.command()
def list():
    data = CliTodoList.list()
    table = Table(title="TODO LIST")
    table.add_column("#", justify="right", style="cyan", no_wrap=True)
    table.add_column("Title", style="magenta")
    table.add_column("Created", justify="right", style="green")
    for item in data:
        table.add_row(f'{item[0]}', f'{item[1]}', f'{item[2]}')
    console = Console()
    console.print(table)


@cli_td.command()
@click.option('--number', '-n', prompt='Number', help='Number todo list.')
def detail(number):
    data = CliTodoList.get_by_id(number)
    if data is None:
        print('TODO LIST NOT FOUND')
        return False
    # table
    title = f'# {data[0]} - {data[1]}'
    print(f'NO TIENES TAREAS EN: {title}')

    table = Table(title=title)
    table.add_column("#", justify="right", style="cyan", no_wrap=True)
    table.add_column("Title", style="blue")
    table.add_column("status", style="magenta")
    table.add_column("Created", justify="right", style="green")
    # data
    data_task = CliTodoList.task_list_by_pk(number)
    for item in data_task:
        table.add_row(f'{item[0]}', f'{item[1]}', f'{item[2]}', f'{item[3]}',)
    console = Console()
    console.print(table)


@cli_td.command()
@click.option('--number', '-n', prompt='Number', help='Number todo list.')
@click.option('--name', prompt='Title', help='New todo list name.')
def new_task(name, number):
    CliTodoList.insert_task(name, number)

