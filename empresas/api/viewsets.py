from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from empresas.models import Empresa
from utils.exceptions.catalogo_exceptions import CustomValidation
from .serializers import EmpresaSerializer
from .service import EmpresaService


class EmpresasViewSet(ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer


    def create(self, request, *arg, **kwargs):
        try:
            empresa = EmpresaService.from_dto(request.data)
            EmpresaService.save_empresa(empresa)
            serializer = EmpresaSerializer(empresa)
            response = {'message': 'Empresa Created', 'result': serializer.data}
            return Response(response, status=status.HTTP_200_OK)
        except Exception as error:
            raise CustomValidation(error, 'detail', status_code=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        try:
            empresa = Empresa.objects.filter(id=kwargs['pk'])[0]
            empresa = EmpresaService.from_dto_update(request.data, empresa)
            EmpresaService.save_empresa(empresa)
            serializer = EmpresaSerializer(empresa)
            response = {'message': 'Empresa Updated', 'result': serializer.data}
            return Response(response, status=status.HTTP_200_OK)
        except Exception as error:
            raise CustomValidation(error, 'detail', status_code=status.HTTP_400_BAD_REQUEST)
