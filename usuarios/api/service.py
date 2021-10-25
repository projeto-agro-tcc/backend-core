from rest_framework import status
from rest_framework.exceptions import APIException

from enderecos.api.service import EnderecoService
from telefones.api.service import TelefoneService
from usuarios.models import Usuario
from utils.exceptions.catalogo_exceptions import CustomValidation


class UsuarioService:

    def __init__(self):
        pass

    def from_dto(objDto):
        error = UsuarioService.validate_user_and_password(objDto)
        if error:
            raise CustomValidation(error, 'detail', status_code=status.HTTP_409_CONFLICT)

        try:
            endereco = EnderecoService.from_dto(objDto)
            telefones = TelefoneService.from_dto(objDto)
            TelefoneService.save_telefones(telefones)
            EnderecoService.save_endereco(endereco)
            user = Usuario()
            user.endereco = endereco
            user.telefone = telefones
            user.cpf = objDto['cpf']
            user.email = objDto['email']
            user.username = objDto['username']
            user.first_name = objDto['first_name']
            user.last_name = objDto['last_name']
            user.set_password(objDto['password'])
            return user
        except Exception as error:
            raise error


    def from_dto_update(objDto, user):
        try:
            user.cpf = objDto['cpf']
            user.email = objDto['email']
            user.username = objDto['username']
            user.first_name = objDto['first_name']
            user.last_name = objDto['last_name']
            endereco = EnderecoService.from_dto_update(objDto, user.endereco)
            telefones = TelefoneService.from_dto_update(objDto, user.telefone)
            TelefoneService.save_telefones(telefones)
            EnderecoService.save_endereco(endereco)
            user.endereco = endereco
            user.telefone = telefones
            return user
        except Exception as error:
            raise error

    def validate_user_and_password(objDto):
        error = []
        if Usuario.objects.filter(username=objDto['username']).exists():
            error.append("Username is not unique")
        if Usuario.objects.filter(email=objDto['email']).exists():
            error.append("Email is not unique")
        if Usuario.objects.filter(cpf=objDto['cpf']).exists():
            error.append("CPF is not unique")
        return error

    def save_usuario(usuario):
        try:
            usuario.save()
        except:
            raise CustomValidation("Erro ao salvar usuário", 'detail', status_code=status.HTTP_409_CONFLICT)
