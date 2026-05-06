import flet as ft
from models.UsersModel import UsuarioModel

def DashboardView(page, tarea_controller):
    page.title = "Tareas"
    user = getattr(page, "user_data")
    lista_tareas = ft.Column(scroll=ft.ScrollMode.ALWAYS, expand=True)
    
    def eliminar(id_tarea):
        success, msg = tarea_controller.eliminar_tarea(id_tarea)
    
        if success:
            refresh()
        else:
            page.snack_bar = ft.SnackBar(ft.Text(msg))
            page.snack_bar.open = True
            page.update()
    
    def refresh():
        if user and 'id_usuario' in user:
            lista_tareas.controls.clear()
            tareas = tarea_controller.obtener_lista(user['id_usuario'])
    
    
            for t in tareas:
                lista_tareas.controls.append(
                    ft.Card(
                        content=ft.Container(
                            content=ft.ListTile(
                                title=ft.Text(t['titulo'], weight="bold"),
                                subtitle=ft.Text(
                                    f"{t['descripcion']}\nPrioridad: {t['prioridad']}"
                                ),
                                trailing=ft.Row(
                                    [
                                        ft.Container(
                                            content=ft.Text(t.get('estado', 'pendiente')),
                                            bgcolor=ft.Colors.ORANGE_300,
                                            padding=5,
                                            border_radius=5
                                        ),
            
                                        ft.IconButton(
                                            icon=ft.Icons.DELETE,
                                            icon_color="red",
                                            on_click=lambda e, id=t['id_tarea']: eliminar(id)
                                        )
                                    ],tight=True
                                )
                            ),
                            padding=10
                        )
                    )
                )
            page.update()
    
    refresh()

    txt_titulo = ft.TextField(label="Nueva Tarea", expand=True)
    descripcion = ft.TextField(label="Descripcion", expand=True)
    prioridad = ft.RadioGroup(
    value="media",
    content=ft.Column([
            ft.Radio(value="alta", label="Alta"),
            ft.Radio(value="media", label="Media"),
            ft.Radio(value="baja", label="Baja"),
        ])
    )
    
    clasificacion = ft.RadioGroup(
        value="Escuela",
        content=ft.Column([
            ft.Radio(value="Escuela", label="Escuela"),
            ft.Radio(value="Trabajo", label="Trabajo"),
            ft.Radio(value="Cotidiano", label="Cotidiano"),
        ])
    )
    
    estado = ft.RadioGroup(
        value="Pendiente",
        content=ft.Column([
            ft.Radio(value="Pendiente", label="Pendiente"),
            ft.Radio(value="Terminada", label="Terminada"),
        ])
    )

    def add_task(e):
        if user and 'id_usuario' in user:
            success, msg = tarea_controller.guardar_nueva(
                user['id_usuario'],
                txt_titulo.value,
                descripcion.value,
                prioridad.value,
                clasificacion.value,
                estado.value,
            )
            if success:
                txt_titulo.value = ""
                descripcion.value = ""
                prioridad.value = ""
                clasificacion.value = ""
                estado.value = ""
                refresh()
            else:
                page.show_dialog(ft.SnackBar(ft.Text(msg)))

    def cerrar_sesion():
        UsuarioModel().cerrar_sesion(user['id_usuario'])
        page.go("/")

    return ft.View(
        route="/dashboard",
        controls=[
            ft.AppBar(
                title=ft.Text(f"Bienvenido, {user['nombre'] if user else 'Usuario'}"),
                
                actions=[
                    ft.IconButton(ft.Icons.PERSON, on_click=lambda _: page.go("/perfil")),
                    ft.IconButton(ft.Icons.EXIT_TO_APP, on_click=cerrar_sesion)
                ],
            ),
            ft.Container(
                ft.Column([
                    ft.Row([
                        txt_titulo,
                        ft.VerticalDivider(thickness=2,color=ft.Colors.BLUE,width=10,),
                        descripcion,
                        ft.VerticalDivider(thickness=2,color=ft.Colors.BLUE,),
                        ft.Column([
                        ft.Text("Prioridad"),
                        prioridad,]),
                        ft.VerticalDivider(thickness=2,color=ft.Colors.BLUE,),
                        ft.Column([
                        ft.Text("Clasificacion"),
                        clasificacion,]),
                        ft.VerticalDivider(thickness=2,color=ft.Colors.BLUE,),
                        ft.Column([
                        ft.Text("Estado"),
                        estado,
                        ft.VerticalDivider(thickness=2,color=ft.Colors.BLUE,),
                        ]),
                        ft.FloatingActionButton(icon=ft.Icons.ADD, on_click=add_task),
                    ], height=130),
                    ft.Divider(),
                    ft.Text("Mis Tareas Pendientes", size=20, weight="bold"),
                    lista_tareas
                ], expand=True),
                padding=20,expand=True
            ),
        ]
    )