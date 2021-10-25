from rest_framework.exceptions import APIException

from enderecos.models import Endereco


class EnderecoService:

    def __init__(self, logradouro=None, numero=None, complemento=None, bairro=None, cidade=None, cep=None, uf=None):
        self.logradouro = logradouro
        self.numero = numero
        self.complemento = complemento
        self.bairro = bairro
        self.cidade = cidade
        self.cep = cep
        self.uf = uf

    def from_dto(objDto):
        try:
            endereco = Endereco()
            endereco.logradouro = objDto['logradouro']
            endereco.numero = objDto['numero']
            endereco.complemento = objDto['complemento']
            endereco.bairro = objDto['bairro']
            endereco.cidade = objDto['cidade']
            endereco.cep = objDto['cep']
            endereco.uf = objDto['uf']
            return endereco
        except:
            raise APIException('Erro parse endereço')

    def from_dto_update(objDto, endereco):
        try:
            endereco = Endereco.objects.filter(id=endereco.id)[0]
            endereco.logradouro = objDto['logradouro']
            endereco.numero = objDto['numero']
            endereco.complemento = objDto['complemento']
            endereco.bairro = objDto['bairro']
            endereco.cidade = objDto['cidade']
            endereco.cep = objDto['cep']
            endereco.uf = objDto['uf']
            return endereco
        except:
            raise APIException('Erro parse endereço')

    def save_endereco(endereco):
        try:
            endereco.save()
        except:
            raise APIException('Problemas ao cadastar endereço')
