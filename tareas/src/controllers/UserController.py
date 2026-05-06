from models.UsersModel import UsuarioModel
from models.schemasModel import UsuarioShema
from pydantic import ValidationError

class AuthController:
    def __init__(self):
        self.model = UsuarioModel()
        
    def registrar_Usuario(self, nombre, apellido, email, contraseña, telefono, fecha):
        try:
            nuevo_usuario = UsuarioShema(
                nombre=nombre,
                apellido=apellido,
                email=email,
                password=contraseña,
                telefono=telefono,
                fecha=fecha
            )

            success = self.model.registrar(nuevo_usuario)
            if success:
                return True, "Usuario creador correctamente, inicia sesion"
            else:
                return False, "Usuario Existente"

        except ValidationError as e:
            return False, e.errors()[0]['msg']
    
    def modificar(self, id_usuario, nombre, apellido, telefono):
        try:
            success = self.model.modificar_perfil(id_usuario, nombre, apellido, telefono)
            return success
        except Exception as e:
            print(f"Error al modificar perfil: {e}")
            return False
    
    def login(self, email, password):
        try:
            print("ENTRÉ AL LOGIN CONTROLLER")
    
            user = self.model.validar_login(email, password)
    
            if user:
                return user, "Login correcto"
            else:
                return False, "Credenciales incorrectas"
    
        except ValidationError as e:
            return False, e.errors()[0]['msg']