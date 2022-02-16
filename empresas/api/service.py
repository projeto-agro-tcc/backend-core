from rest_framework import status

from empresas.models import Empresa
from enderecos.api.service import EnderecoService
from telefones.api.service import TelefoneService
from utils.exceptions.catalogo_exceptions import CustomValidation


class EmpresaService:

    def __init__(self):
        pass

    def from_dto(objDto):
        error = EmpresaService.validate_empresa(objDto)
        if error:
            raise Exception(error)

        try:
            empresa = Empresa()
            empresa.endereco = EnderecoService.from_dto(objDto)
            empresa.telefone = TelefoneService.from_dto(objDto)
            empresa.nome = objDto['nome']
            empresa.cnpj = objDto['cnpj']
            empresa.email = objDto['email']
            empresa.web_site = objDto['web_site']
            return empresa
        except Exception as error:
            raise CustomValidation(error, 'detail', status_code=status.HTTP_400_BAD_REQUEST)

    def from_dto_update(objDto, empresa):
        try:
            empresa = Empresa.objects.filter(id=empresa.id)[0]
            empresa.endereco = EnderecoService.from_dto_update(objDto, empresa.endereco)
            empresa.telefone = TelefoneService.from_dto_update(objDto, empresa.telefone)
            empresa.nome = objDto['nome']
            empresa.cnpj = objDto['cnpj']
            empresa.email = objDto['email']
            empresa.web_site = objDto['web_site']
            return empresa
        except Exception as error:
            raise CustomValidation(error, 'detail', status_code=status.HTTP_400_BAD_REQUEST)

    def save_empresa(empresa):
        try:
            TelefoneService.save_telefones(empresa.telefone)
            EnderecoService.save_endereco(empresa.endereco)
            empresa.save()
        except Exception as error:
            raise CustomValidation(error, 'detail', status_code=status.HTTP_409_CONFLICT)

    def validate_empresa(objDto):
        error = []
        if Empresa.objects.filter(cnpj=objDto['cnpj']).exists():
            error.append("CNPJ is not unique")
        if Empresa.objects.filter(email=objDto['email']).exists():
            error.append("email is not unique")
        if Empresa.objects.filter(web_site=objDto['web_site']).exists():
            error.append("web_site is not unique")
        return error

    def delete_empresa(empresa):
        try:
            empresa.status = 0
            empresa.save()
        except:
            raise CustomValidation("Erro ao deletar empresa", 'detail', status_code=status.HTTP_409_CONFLICT)
