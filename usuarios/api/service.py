from enderecos.api.service import EnderecoService
from telefones.api.service import TelefoneService
from usuarios.models import Usuario


class UsuarioService:

    def __init__(self):
        pass

    def from_dto(objDto):
        endereco = EnderecoService.from_dto(objDto)
        telefones = TelefoneService.from_dto(objDto)
        endereco.save()
        telefones.save()
        user = Usuario()
        user.endereco = endereco
        user.telefone = telefones
        user.cpf = objDto['cpf']
        user.username = objDto['username']
        user.first_name = objDto['first_name']
        user.last_name = objDto['last_name']
        return user
