from rest_framework.exceptions import APIException

from telefones.models import Telefone


class TelefoneService:

    def __init__(self, residencial=None, celular=None, outro=None):
        self.residencial = residencial
        self.celular = celular
        self.outro = outro

    def from_dto(objdto):
        try:
            telefones = Telefone()
            telefones.residencial = objdto['residencial']
            telefones.celular = objdto['celular']
            telefones.outro = objdto['outro']
            return telefones
        except:
            raise APIException('Erro parse telefones')

    def from_dto_update(objdto, telefone):
        try:
            telefones = Telefone.objects.filter(id=telefone.id)[0]
            telefones.residencial = objdto['residencial']
            telefones.celular = objdto['celular']
            telefones.outro = objdto['outro']
            return telefones
        except:
            raise APIException('Erro parse telefones')

    def save_telefones(telefones):
        try:
            telefones.save()
        except:
            raise APIException('Problemas ao cadastar telefone')
