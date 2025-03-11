import flet as ft

def main (page: ft.Page):

    class MyButton(ft.ElevatedButton):
        def __init__(self, text, on_click):
            super().__init__()
            self.bgcolor = ft.Colors.ORANGE_300
            self.color = ft.Colors.GREEN_800
            self.text = text
            self.on_click = on_click
    
        
    def ok_clicked(e):
            
        text_field.value = 'Ok, clicked!' 
        page.add(text_field)       

        #print("Ok, clicked!")

    def cancel_clicked (e):
        
        text_field.value = 'Cancel, clicked!'
        page.add(text_field)
        #print("Cancel, clicked")

    
    text_field = ft.TextField(label='Outcome here!')
    page.add(
        MyButton(text = "OK", on_click= ok_clicked),
        MyButton(text = "Cancel", on_click=cancel_clicked), text_field
        )

ft.app(main)