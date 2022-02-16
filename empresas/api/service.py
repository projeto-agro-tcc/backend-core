from empresas.models import Empresa
from enderecos.api.service import EnderecoService
from telefones.api.service import TelefoneService


class EmpresaService:

    def __init__(self):
        self.endereco_service = EnderecoService()
        self.telefone_service = TelefoneService()

    def from_dto(self, objDto):
        error = self.validate_empresa(objDto)
        if error:
            raise Exception(error)

        try:
            empresa = Empresa()
            empresa.endereco = self.endereco_service.from_dto(objDto)
            empresa.telefone = self.telefone_service.from_dto(objDto)
            empresa.nome = objDto['nome']
            empresa.cnpj = objDto['cnpj']
            empresa.email = objDto['email']
            empresa.web_site = objDto['web_site']
            return empresa
        except Exception:
            raise Exception("Problems convert empresa dto")

    def from_dto_update(self, objDto, empresa):
        try:
            empresa = Empresa.objects.filter(id=empresa.id)[0]
            empresa.endereco = self.endereco_service.from_dto_update(objDto, empresa.endereco)
            empresa.telefone = self.telefone_service.from_dto_update(objDto, empresa.telefone)
            empresa.nome = objDto['nome']
            empresa.cnpj = objDto['cnpj']
            empresa.email = objDto['email']
            empresa.web_site = objDto['web_site']
            return empresa
        except Exception:
            raise Exception("Problems convert empresa dto")

    def save_empresa(self, empresa):
        try:
            self.telefone_service.save_telefones(empresa.telefone)
            self.endereco_service.save_endereco(empresa.endereco)
            empresa.save()
        except Exception:
            raise Exception("Problems to save empresa")

    def validate_empresa(self, objDto):
        error = []
        if Empresa.objects.filter(cnpj=objDto['cnpj']).exists():
            error.append("CNPJ is not unique")
        if Empresa.objects.filter(email=objDto['email']).exists():
            error.append("email is not unique")
        if Empresa.objects.filter(web_site=objDto['web_site']).exists():
            error.append("web_site is not unique")
        return error

    def delete_empresa(self, empresa):
        try:
            empresa.status = 0
            empresa.save()
        except:
            raise Exception("Error to delete empresa")
