import flet as ft

def main (page: ft.Page):

    class MyButton(ft.ElevatedButton):
        def __init__(self, text):
            super().__init__()
            self.bgcolor = ft.Colors.ORANGE_300
            self.color = ft.Colors.GREEN_800
            self.text = text

    page.add(MyButton(text="OK"), MyButton(text="Cancel"))


ft.app(main)