from rest_framework.exceptions import APIException

from enderecos.api.service import EnderecoService
from telefones.api.service import TelefoneService
from usuarios.models import Usuario


class UsuarioService:

    def __init__(self):
        pass

    def from_dto(objDto):
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
        except:
            raise APIException('Problemas converter objeto UsuarioDto')


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
        except:
            raise APIException('Problemas ao editar Usuário')
