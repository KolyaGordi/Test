import flet as ft

def main(page: ft.Page):
    flashlight = ft.Flashlight()
    page.overlay.append(flashlight)
    page.add(
        ft.ElevatedButton(text='asdasdad', on_click=lambda _: flashlight.toggle())
    )

ft.app(target=main, view=ft.AppView.WEB_BROWSER)
