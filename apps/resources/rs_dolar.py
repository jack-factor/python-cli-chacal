from bs4 import BeautifulSoup
from rich.console import Console
from rich.progress import track
from rich.table import Table
from time import sleep
from apps.resources.general_params import URL_BCR_DOLAR
import requests


class CliDolar():

    def _get_data():
        req = requests.get(URL_BCR_DOLAR)
        soup = BeautifulSoup(req.text, 'html.parser')
        body_html = soup.body
        data = body_html.find('table',
                              id="ctl00_cphContent_rgTipoCambio_ctl00")
        result = []
        for tr in data.findAll('tr'):
            value_list = []
            for td in tr.findAll('td'):
                value_list.append(td.text)
            if len(value_list) == 3:
                result.append(value_list)
        return result

    def show_table():
        data = CliDolar._get_data()
        # progress
        for i in track(range(100), description='[green]Processing data'):
            if i and i % 99 == 0:
                print(i)
            sleep(0.01)
        # table
        console = Console()
        table = Table(title="El dolar hoy")
        table.add_column("Moneda", style="cyan", no_wrap=True)
        table.add_column("Venta", justify="right", style="magenta")
        table.add_column("Compra", justify="right", style="green")
        # read
        for item in data:
            table.add_row(item[0], item[1], item[2])
        console.print(table)
