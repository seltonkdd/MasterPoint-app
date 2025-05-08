from datetime import datetime
import flet as ft
import os

from components import StartContainer, MainContainer
from datatable import table_column, show_db
from gps import get_location_image_backend, get_geolocator
from services import Client


IMAGE_PATH = 'assets/imagem_gps.png'


def main(page: ft.Page):
   # Configuração inicial da página
    page.window.width, page.window.height = 400, 800
    page.expand = True
    page.overlay.append(ft.SnackBar(ft.Text()))
    snack_bar = page.overlay[0]

    client = Client()
    gl = get_geolocator()
    page.overlay.append(gl)

    timefield = ft.Ref[ft.Row]()

    # Funções auxiliares
    def view_pop(view):
        if len(page.views) > 1:
            page.views.pop()
            page.go(page.views[-1].route)
            page.update()
        hide_timefield()

    def show_snack_bar(message, color):
        snack_bar.content.value, snack_bar.bgcolor, snack_bar.open = message, color, True
        page.update()

    def clean_fields(e):
        for field in [_login.email_field, _login.senha_field]:
            field.value = ""

    def toggle_main(e):
        # MOSTRAR TELA PRINCIPAL
        clean_fields(e)
        listar_pontos()
        page.go('/main')

    def animate_main(e):
        # ANIMAR NAVEGAÇÃO DA TELA PRINCIPAL
        _tableview.offset=ft.transform.Offset(-5,0)
        _main.offset=ft.transform.Offset(0,0)
        page.update()

    def toggle_tableview(e):
        # MOSTRAR TELA DA TABELA
        listar_pontos()
        _tableview.offset=ft.transform.Offset(0,0)
        _main.offset=ft.transform.Offset(2,0)
        page.update()

    def hide_timefield():
        timefield.current.visible = False
        timefield.current.update()

    def handle_time_change(e):
        timefield.current.visible = True
        timefield.current.controls[0].value = time_picker.value
        page.update()

    def reset_time_picker():
        time_picker.value = datetime.now()
        time_picker.update()

    def handle_get_current_position(e):
        if os.path.exists(IMAGE_PATH):
            os.remove(IMAGE_PATH)
        try:
            p = gl.get_current_position()
            if p:
                get_location_image_backend(p.latitude, p.longitude)
                _main.update()
        except:
            page.open(app_settings_dlg)

    def handle_open_app_settings(e):
        #ABRIR AS CONFIGURAÇÕES DE LOCALIZAÇÃO
        gl.open_location_settings()
        page.close(app_settings_dlg)

    app_settings_dlg = ft.AlertDialog(
        adaptive=True,
        content=ft.Text('Não foi possível acessar sua localização. Permita o app obte-la nas configurações.'),
        actions=[ft.TextButton(text="Abrir configurações", on_click=handle_open_app_settings)],
        actions_alignment=ft.MainAxisAlignment.CENTER,
    )

    # Requisições para servidor
    def login_usuario(e):
        email, senha = _login.email_field.value, _login.senha_field.value
        data = {"email": email, "password": senha}
        if not email or not senha:
            show_snack_bar("O campo email e senha são obrigatórios.", 'red')
            return
        resposta = client.post_request('auth/token/', data)
        if not resposta:
            show_snack_bar('Login bem-sucedido', 'green')
            toggle_main(e)
            handle_get_current_position(e)
        else:
            show_snack_bar(resposta, 'red')

    def registrar_ponto():
        p = None
        try:
            p = gl.get_current_position()
        finally:
            latitude = None
            longitude = None
            if p:
                latitude = p.latitude
                longitude = p.longitude

            data = {
                "punch": f'{datetime.now().date()} {time_text.value}',
                "latitude": f'{latitude}',
                "longitude": f'{longitude}'
                }
            
            resposta = client.post_request('clocks/', data)
            if not resposta:
                show_snack_bar('Ponto registrado com sucesso!', 'green')
            else:
                show_snack_bar(resposta, 'red')
            hide_timefield()

    def listar_pontos():
        resposta, status_code = client.get_request('clocks/')
        if status_code == 200:
            show_db(resposta)
        else:
            show_snack_bar(resposta, 'red')


    bottom_appbar = ft.BottomAppBar(
        content=ft.Row([
        ft.IconButton(icon=ft.Icons.LIST_ALT, scale=1.5, on_click=toggle_tableview),
        ft.IconButton(icon=ft.Icons.LOCK_CLOCK, scale=1.5, on_click=animate_main)
        ], alignment=ft.MainAxisAlignment.CENTER, spacing=100),
        height=63,
    )

    time_picker = ft.TimePicker(
        confirm_text="Confirm",
        error_invalid_text="Time out of range",
        on_change=handle_time_change
    )
    time_text = ft.Text(style=ft.TextStyle(weight=ft.FontWeight.BOLD))
    timefield.current = ft.Row(
        [
            time_text,
            ft.TextButton("Salvar", on_click=lambda e: registrar_ponto())
        ], alignment=ft.MainAxisAlignment.CENTER
    )

    # container de login
    _login = StartContainer(title='Faça Login', submit_text='Login', func=login_usuario)

    # container principal
    _main = MainContainer(
        height=page.height,
        controls=[
            ft.Text('Bata seu ponto', size=30, weight=10),
            ft.Card(
                width=page.width,
                elevation=20,
                content=ft.Column(
                    [
                        ft.Container(ft.Image(IMAGE_PATH, scale=0.899), expand=True, alignment=ft.alignment.center),
                        ft.Row(
                            [
                                ft.TextButton("Localização", on_click=handle_get_current_position),
                                ft.TextButton("Ponto", on_click=lambda e: (reset_time_picker(), 
                                                                        page.open(time_picker)))
                            ], alignment=ft.MainAxisAlignment.END
                        )
                    ], horizontal_alignment='center'
                )
            ),
            timefield.current
        ]
    )
    
    # container da tabela
    _tableview = MainContainer(
        height=page.height,
        offset=[-5, 0],
        controls=[
            ft.Container(
                content=table_column, 
                alignment=ft.alignment.center, 
                margin=0, 
                height=600
            )
        ]
    )

    _about = ft.Container(
        height=page.height,
        expand=True,
        content=ft.Column(
            [
                ft.Text('MasterPoint', size=30, style=ft.TextStyle(weight=ft.FontWeight.BOLD)),
                ft.Text('Versão 1.0.0', opacity=0.5),
                ft.Image('leading.png', color='grey', height=90, width=90),
                ft.Text('© 2025 MasterPoint Inc.', opacity=0.5)                               
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER
        )
    )

    def route_change(event: ft.RouteChangeEvent):
        appbar = ft.AppBar(
                        title=ft.Text('MasterPoint', size=25),
                        center_title=True,
                        bgcolor=ft.Colors.ON_INVERSE_SURFACE,
                        actions=[
                            ft.PopupMenuButton(items=[
                                ft.PopupMenuItem(icon=ft.Icons.INFO,
                                                text='Sobre',
                                                on_click=lambda _: page.go('/about'))
                                                ])])

        routes = {
            '/': ft.View(
                '/', [appbar, _login],
                vertical_alignment='center'),
            '/main': ft.View(
                '/main', [appbar, 
                          ft.Stack(controls=[
                              _main, 
                              _tableview
                              ], expand=True, alignment=ft.alignment.center), 
                          time_picker, bottom_appbar],
                vertical_alignment='center'),
            '/about': ft.View(
                    '/about', [appbar, _about], horizontal_alignment='center')
            }

        route = event.route
        if page.views[0].route not in routes:
            page.views.pop()
        if not any(view.route == page.route for view in page.views):
            if page.route in routes:
                page.views.append(routes[route])
        page.update()

    def event(e):
        if e.data=='detach' and page.platform == ft.PagePlatform.ANDROID:
            os._exit(1)


    page.on_app_lifecycle_state_change = event
    timefield.current.visible = False
    page.on_view_pop = view_pop
    page.on_route_change = route_change
    page.go('/')

ft.app(target=main)
