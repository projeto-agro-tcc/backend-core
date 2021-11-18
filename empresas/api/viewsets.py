from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from empresas.models import Empresa
from utils.exceptions.catalogo_exceptions import CustomValidation
from .serializers import EmpresaSerializer
from .service import EmpresaService
from utils.permissions.permissions import authenticated_user, allowed_users_by_group


class EmpresasViewSet(ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer
    authentication_classes = (TokenAuthentication,)

    @authenticated_user
    @allowed_users_by_group(allowed_roles=['admin', 'super_user'])
    def create(self, request, *arg, **kwargs):
        try:
            empresa = EmpresaService.from_dto(request.data)
            EmpresaService.save_empresa(empresa)
            serializer = EmpresaSerializer(empresa)
            response = {'message': 'Empresa Created', 'result': serializer.data}
            return Response(response, status=status.HTTP_200_OK)
        except Exception as error:
            raise CustomValidation(error, 'detail', status_code=status.HTTP_400_BAD_REQUEST)


    @authenticated_user
    @allowed_users_by_group(allowed_roles=['admin', 'high_user', 'super_user'])
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

    @authenticated_user
    @allowed_users_by_group(allowed_roles=['admin', 'super_user'])
    def destroy(self, request, *args, **kwargs):
        try:
            empresa = Empresa.objects.filter(id=kwargs['pk'])[0]
            EmpresaService.delete_empresa(empresa)
            return Response(status=status.HTTP_200_OK)
        except Exception as err:
            raise CustomValidation(err, 'detail', status_code=status.HTTP_400_BAD_REQUEST)

    @authenticated_user
    def list(self, request, *args, **kwargs):
        role_list = request.user.groups.all()
        for role in role_list:
            if role.name in ['admin', 'super_user']:
                queryset = Empresa.objects.filter(status=1)
                serializer = EmpresaSerializer(queryset, many=True)
                return Response(serializer.data)
        else:
            queryset = Empresa.objects.filter(status=1).filter(usuario=request.user)
            serializer = EmpresaSerializer(queryset, many=True)
            return Response(serializer.data)
