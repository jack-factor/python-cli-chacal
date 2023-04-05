from apps.resources.rs_dolar import CliDolar
import click


@click.group()
def cli_dl():
    pass


@cli_dl.command()
def dolar():
    CliDolar.show_table()
    click.echo('Fuente pagína web del BCR')
