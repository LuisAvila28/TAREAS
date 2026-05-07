import flet as ft

def LoginView(page: ft.Page, auth_controller):
    
    correo = ft.TextField(
        label="Correo electrónico",
        prefix_icon=ft.Icons.PERSON,
        width=400,
        border_radius=10,
        keyboard_type=ft.KeyboardType.EMAIL,
        border_color=ft.Colors.GREEN_300
    )

    contraseña = ft.TextField(
        label="Contraseña",
        prefix_icon=ft.Icons.KEY,
        password=True,
        can_reveal_password=True,
        width=400,
        border_radius=10,
        border_color=ft.Colors.GREEN_300
    )

    mensaje = ft.Text("", color=ft.Colors.GREEN_300)

    def mostrar_snackbar(mensaje_texto, color=ft.Colors.GREEN_400):
        page.snack_bar = ft.SnackBar(
            content=ft.Text(mensaje_texto),
            bgcolor=color,
            duration=2000,
        )
        page.snack_bar.open = True
        page.update()

    def login_click(e):
        if not correo.value or not contraseña.value:
            mensaje.value = "Por favor, llene todos los campos"
            mensaje.color = ft.Colors.GREEN_300
            page.update()
            return
        
        user, msg = auth_controller.login(correo.value, contraseña.value)
        if user:
            page.user_data = user
            mostrar_snackbar("¡Sesión iniciada correctamente!", ft.Colors.GREEN_400)
            page.go("/dashboard")
        else:
            mensaje.value = msg
            mensaje.color = ft.Colors.GREEN_300
            page.update()

    iniciar_sesion = ft.ElevatedButton(
        "Iniciar sesión",
        width=250,
        on_click=login_click,
        style=ft.ButtonStyle(
            bgcolor=ft.Colors.GREEN_400,
            color=ft.Colors.WHITE,
            padding=20,
            shape=ft.RoundedRectangleBorder(radius=12),
        ),
    )

    btn_registro = ft.TextButton(
        "¿No tienes cuenta? Regístrate",
        on_click=lambda _: page.go("/register"),
        style=ft.ButtonStyle(
            color=ft.Colors.GREEN_400
        )
    )

    contraseña.on_submit = login_click

    return ft.View(
        route="/",
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        appbar=ft.AppBar(
            title=ft.Text("SIGE - Inicio Sesion"),
            bgcolor=ft.Colors.GREEN_400,
            color=ft.Colors.WHITE
        ),
        controls=[
            ft.Column(
                [
                    ft.Icon(
                        icon=ft.Icons.AUTO_AWESOME,
                        size=60,
                        color=ft.Colors.GREEN_400
                    ),

                    ft.Container(height=10),

                    ft.Text("Inicia Sesion", size=24, weight="bold", color=ft.Colors.GREEN_400),
                    ft.Container(height=10),

                    correo,
                    ft.Container(height=10),

                    contraseña,
                    ft.Container(height=10),

                    mensaje,
                    ft.Container(height=10),

                    ft.Row(
                        [iniciar_sesion],
                        alignment=ft.MainAxisAlignment.CENTER
                    ),

                    ft.Container(height=10),

                    btn_registro
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                tight=True,
                spacing=10
            )
        ]
    )
