from rest_framework import status
from enderecos.models import Endereco
from utils.exceptions.catalogo_exceptions import CustomValidation


class EnderecoService:

    def __init__(self, logradouro=None, numero=None, complemento=None, bairro=None, cidade=None, cep=None, uf=None):
        self.logradouro = logradouro
        self.numero = numero
        self.complemento = complemento
        self.bairro = bairro
        self.cidade = cidade
        self.cep = cep
        self.uf = uf

    def from_dto(self, objDto):
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
            raise CustomValidation("Erro ao parse endereço", 'detail', status_code=status.HTTP_400_BAD_REQUEST)

    def from_dto_update(self, objDto, endereco):
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
            raise CustomValidation("Erro ao parse endereço", 'detail', status_code=status.HTTP_400_BAD_REQUEST)

    def save_endereco(self, endereco):
        try:
            endereco.save()
        except:
            raise CustomValidation("Erro ao salvar endereço", 'detail', status_code=status.HTTP_409_CONFLICT)
