import flet as ft
from datetime import datetime

def RegistroView(page: ft.Page, auth_controller):
    
    def ver_contra():
        contra.password = not contra.password
        contra.update()
        
    correo=(ft.TextField(label="Correo",autofocus=True, icon=ft.Icons.PERSON ))
    contra=(ft.TextField(label="Contraseña",suffix=ft.IconButton(icon=ft.Icons.VISIBILITY, on_click=ver_contra) ,password=True, autofocus=True, icon=ft.Icons.PASSWORD))
    nombre=(ft.TextField(label="Nombre",icon=ft.Icons.BADGE))
    apellido=(ft.TextField(label="apellido",autofocus=True,))
    telefono=(ft.TextField(label="Telefono",autofocus=True,icon=ft.Icons.CALL))
    file_picker = ft.FilePicker()
    boton = ft.Button("Seleccionar Archivo", on_click=lambda _: file_picker.pick_files(allow_multiple=True, allowed_extensions=[".jpg", ".jpeg", ".png"]))
    
    def registra(e):
        if not correo.value and not contra.value and not nombre.value and not apellido.value and not telefono.value :
            page.show_dialog(ft.SnackBar(ft.Text("Por favor, complete todos los campos")))
            return
        
        hoy = datetime.now()
        fecha = hoy.strftime("%Y-%m-%d")
        
        user, msg = auth_controller.registrar_Usuario(nombre.value, apellido.value, correo.value, contra.value, telefono.value, fecha)
        
        if user:
            page.go("/")
            page.show_dialog(ft.SnackBar(ft.Text(msg)))
        else:
            page.show_dialog(ft.SnackBar(ft.Text(msg)))
    
    registrar =( ft.ElevatedButton("Registrase",color=ft.Colors.BLUE, on_click=registra))
    def regresar():
        page.go("/")
        
    reversa = ( ft.ElevatedButton("Regresar a login",color=ft.Colors.RED ,on_click=regresar))
    
    return ft.View(
        route="/registro",
        vertical_alignment=ft.MainAxisAlignment.CENTER, 
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        appbar=ft.AppBar(
            title=ft.Text("Registro"),
            bgcolor=ft.Colors.BLUE_GREY_900,
            color="white"
        ),
        controls=[
            ft.Column(
                [
                    ft.Icon(ft.Icons.ACCOUNT_BOX, size=50, color=ft.Colors.BLUE),
                    ft.Text("Registro de usuario", size=30, weight="bold"),
                    ft.Row([nombre,apellido,],ft.CrossAxisAlignment.CENTER,),
                    telefono,
                    correo,
                    contra,
                    boton,
                    registrar,
                    reversa
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20,
                tight=True 
            )
        ]
    )
    