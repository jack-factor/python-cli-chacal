from apps.commands.cli_todo import cli_td
from apps.resources.rs_dolar import CliDolar
import click


@click.group()
def cli():
    pass


@cli.command()
def dolar():
    CliDolar.show_table()
    click.echo('Fuente pagína web del BCR')


cli.add_command(cli_td, 'todo')
