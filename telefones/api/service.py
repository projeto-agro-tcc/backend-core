from rest_framework import status
from rest_framework.exceptions import ValidationError, APIException

from telefones.models import Telefone
from utils.exceptions.catalogo_exceptions import CustomValidation


class TelefoneService:

    def __init__(self, residencial=None, celular=None, outro=None):
        self.residencial = residencial
        self.celular = celular
        self.outro = outro

    def from_dto(self, objdto):
        try:
            telefones = Telefone()
            telefones.residencial = objdto['residencial']
            telefones.celular = objdto['celular']
            telefones.outro = objdto['outro']
            return telefones
        except:
            raise CustomValidation("Erro ao parse telefones", 'detail', status_code=status.HTTP_400_BAD_REQUEST)

    def from_dto_update(self, objdto, telefone):
        try:
            telefones = Telefone.objects.filter(id=telefone.id)[0]
            telefones.residencial = objdto['residencial']
            telefones.celular = objdto['celular']
            telefones.outro = objdto['outro']
            return telefones
        except:
            raise CustomValidation("Erro ao parse telefones", 'detail', status_code=status.HTTP_400_BAD_REQUEST)

    def save_telefones(self, telefones):
        try:
            telefones.save()
        except:
            raise CustomValidation("Erro ao salvar telefone", 'detail', status_code=status.HTTP_409_CONFLICT)
