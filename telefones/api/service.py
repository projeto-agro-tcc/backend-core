from telefones.models import Telefone


class TelefoneService:

    def __init__(self, residencial=None, celular=None, outro=None):
        self.residencial = residencial
        self.celular = celular
        self.outro = outro

    def from_dto(objdto):
        telefones = Telefone()
        telefones.residencial = objdto['residencial']
        telefones.celular = objdto['celular']
        telefones.outro = objdto['outro']
        return telefones

    def from_dto_update(objdto, telefone):
        telefones = Telefone.objects.filter(id=telefone.id)[0]
        telefones.residencial = objdto['residencial']
        telefones.celular = objdto['celular']
        telefones.outro = objdto['outro']
        return telefones
