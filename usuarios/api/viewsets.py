from django.contrib.auth.models import Group
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from usuarios.api.serializers import UsuarioSerializer
from usuarios.api.service import UsuarioService
from usuarios.models import Usuario


class UsuariosViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    def create(self, request, *arg, **kwargs):
        try:
            user = UsuarioService.from_dto(request.data)
            UsuarioService.save_usuario(user)
            my_group = Group.objects.get(name='less_user')
            my_group.user_set.add(user)
            Token.objects.create(user=user)
            serializer = UsuarioSerializer(user)
            response = {'message': 'User Created', 'result': serializer.data}
            return Response(response, status=status.HTTP_200_OK)
        except Exception as err:
            raise err


    def update(self, request, *args, **kwargs):
        try:
            user = Usuario.objects.filter(id=kwargs['pk'])[0]
            user = UsuarioService.from_dto_update(request.data, user)
            UsuarioService.save_usuario(user)
            serializer = UsuarioSerializer(user)
            response = {'message': 'User Updated', 'result': serializer.data}
            return Response(response, status=status.HTTP_200_OK)
        except Exception as err:
            raise err
