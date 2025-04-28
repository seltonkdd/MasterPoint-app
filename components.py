import flet as ft


class StartContainer(ft.Container):
    def __init__(self,  title: str, submit_text: str, func):
        super().__init__()

        self.padding = 10

        self.title = ft.Text(title, weight=30, size=35, text_align=ft.TextAlign.CENTER)
        self.email_field = ft.TextField(label='Email')
        self.senha_field = ft.TextField(label='Senha', password=True, can_reveal_password=True)

        self.confirm_button = ft.ElevatedButton(text=submit_text, width=150, on_click=func)

        elementos = [self.title, self.email_field, self.senha_field, self.confirm_button]

        self.content = ft.Column(
                elementos, horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )


class MainContainer(ft.Container):
    def __init__(self, height: int, controls, offset=[0,0]):
        super().__init__()

        self.height = height
        self.expand = True
        self.offset = ft.transform.Offset(offset[0], offset[1])
        self.animate_offset=ft.animation.Animation(400,curve='easyIn')
        self.alignment = ft.alignment.center

        self.content = ft.Column(controls)
