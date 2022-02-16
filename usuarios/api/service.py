from enderecos.api.service import EnderecoService
from telefones.api.service import TelefoneService
from usuarios.models import Usuario


class UsuarioService:

    def __init__(self):
        self.endereco_service = EnderecoService()
        self.telefone_service = TelefoneService()

    def from_dto(self, objDto):
        error = UsuarioService.validate_user_and_password(self, objDto)
        if error:
            raise Exception(error)

        try:
            user = Usuario()
            user.endereco = self.endereco_service.from_dto(objDto)
            user.telefone = self.telefone_service.from_dto(objDto)
            user.cpf = objDto['cpf']
            user.email = objDto['email']
            user.username = objDto['username']
            user.first_name = objDto['first_name']
            user.last_name = objDto['last_name']
            user.set_password(objDto['password'])
            return user
        except Exception as error:
            raise Exception("Problems saving user")


    def from_dto_update(self, objDto, user):
        try:
            user.cpf = objDto['cpf']
            user.email = objDto['email']
            user.username = objDto['username']
            user.first_name = objDto['first_name']
            user.last_name = objDto['last_name']
            endereco = self.endereco_service.from_dto_update(objDto, user.endereco)
            telefones = self.telefone_service.from_dto_update(objDto, user.telefone)
            self.telefone_service.save_telefones(telefones)
            self.endereco_service.save_endereco(endereco)
            user.endereco = endereco
            user.telefone = telefones
            return user
        except Exception:
            raise Exception("Problem updating user")

    def validate_user_and_password(self, objDto):
        error = []
        if Usuario.objects.filter(username=objDto['username']).exists():
            error.append("Username is not unique")
        if Usuario.objects.filter(email=objDto['email']).exists():
            error.append("Email is not unique")
        if Usuario.objects.filter(cpf=objDto['cpf']).exists():
            error.append("CPF is not unique")
        return error

    def save_usuario(self, usuario):
        self.telefone_service.save_telefones(usuario.telefone)
        self.endereco_service.save_endereco(usuario.endereco)
        usuario.save()

    def delete_user(self, usuario):
        try:
            usuario.is_active = False
            usuario.save()
        except:
            raise Exception("Problem to delete user")
