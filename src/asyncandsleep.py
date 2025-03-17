import asyncio
import flet as ft

def main(page: ft.Page):
    async def button_click(e):
        await asyncio.sleep(20)
        page.add(ft.Text("Hello!"))

    page.add(
        ft.ElevatedButton("Say hello with delay!", on_click=button_click)
    )

ft.app(main)