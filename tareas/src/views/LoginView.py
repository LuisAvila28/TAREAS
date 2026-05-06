import flet as ft
from views.RegistroView import RegistroView
from datetime import datetime


def LoginView(page: ft.Page, auth_controller):
    
    def ver_contra():
        contra.password = not contra.password
        contra.update()
        
    correo=(ft.TextField(label="Correo",autofocus=True, icon=ft.Icons.PERSON ))
    contra=(ft.TextField(label="Contraseña",suffix=ft.IconButton(icon=ft.Icons.VISIBILITY, on_click=ver_contra) ,password=True, autofocus=True, icon=ft.Icons.PASSWORD))
    
    
    
    def login_click(e):
        if not correo.value or not contra.value:
            page.show_dialog(ft.SnackBar(ft.Text("Por favor, complete todos los campos")))
            return
        
    
        user, msg = auth_controller.login(correo.value, contra.value)
    
        if user:
            page.user_data = user
            page.go("/dashboard")
        else:
            page.show_dialog(ft.SnackBar(ft.Text(msg)))
            
    def olvidado():
        page.show_dialog(ft.SnackBar(ft.Text("Se a enviado su contraseña al correo")))
    
    def registro():
        page.go("/registro")
    
    iniciar=( ft.Button("Iniciar sesion",color=ft.Colors.WHITE ,bgcolor=ft.Colors.BLUE,on_click=login_click))
    registrarse =( ft.TextButton("¿Quieres registrarte?", on_click=registro))
    olvidada =( ft.TextButton("¿Olvidaste la contraseña?", on_click=olvidado))
    
    return ft.View(
        route="/",
        vertical_alignment=ft.MainAxisAlignment.CENTER, 
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        appbar=ft.AppBar(
            title=ft.Text("Login"),
            bgcolor=ft.Colors.BLUE_GREY_900,
            color="white"
        ),
        controls=[
            ft.Column(
                [
                    ft.Icon(ft.Icons.LOCK_PERSON, size=50, color=ft.Colors.BLUE),
                    ft.Text("Acceso al sistema", size=24, weight="bold"),
                    correo,
                    contra,
                    iniciar,
                    registrarse,
                    olvidada
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20,
                tight=True 
            )
        ]
    )
    