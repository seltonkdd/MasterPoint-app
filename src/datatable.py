import flet as ft
from datetime import datetime

table_pontos =ft.DataTable(
    columns=[
        ft.DataColumn(ft.Text('ID')),
        ft.DataColumn(ft.Text('Ponto')),
        ft.DataColumn(ft.Text('Usuário'))
    ],
    rows=[], key='pontos'
)

def format_datetime(value):
    dt = datetime.fromisoformat(value)
    return dt.strftime("%d/%m/%Y às %H:%M:%S")

def populate_table(table, keys, data):
    table.rows.clear()
    for p in data:
        row_cells = [
            ft.DataCell(ft.Text(format_datetime(p[field])) if "T" in str(p[field]) else ft.Text(str(p[field])))
            for field in keys
        ]
        table.rows.append(ft.DataRow(cells=row_cells))

def show_db(pontos):
    keys_pontos = ['id', 'punch', 'email']
    populate_table(table_pontos, keys_pontos, pontos)

table_column = ft.Column(
    [
        ft.Row([table_pontos], scroll='always')
    ], scroll=ft.ScrollMode.ALWAYS)
