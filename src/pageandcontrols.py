import flet as ft

def main (page):

    #t = ft.Text(value="Hello, Marco Sena", color= "black blue") #cria-se uma instância com parâmetros que, na realidade, 
                                                                #são as propriedades do objeto criado.
    #page.controls.append(t) #depois, adiciona-se esse controle a lista de controles da página.

    def add_clicked(e):
        page.add(ft.Checkbox(label= new_task.value))
        new_task.value =""
        new_task.focus()
        new_task.update()
            
    
    new_task = ft.TextField(hint_text = "What's needs to be done?", width=300)
    page.add(ft.Row([new_task, ft.ElevatedButton("Add", on_click= add_clicked)]))
    

ft.app(main)