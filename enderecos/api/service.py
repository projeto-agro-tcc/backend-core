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
        endereco = Endereco()
        endereco.logradouro = objDto['logradouro']
        endereco.numero = objDto['numero']
        endereco.complemento = objDto['complemento']
        endereco.bairro = objDto['bairro']
        endereco.cidade = objDto['cidade']
        endereco.cep = objDto['cep']
        endereco.uf = objDto['uf']
        return endereco
