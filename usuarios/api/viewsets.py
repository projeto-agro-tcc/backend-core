from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from usuarios.api.serializers import UsuarioSerializer
from usuarios.api.service import UsuarioService
from usuarios.models import Usuario


class UsuariosViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    def create(self, request, *arg, **kwargs):
        user = UsuarioService.from_dto(request.data)
        user.save()
        serializer = UsuarioSerializer(user)
        response = {'message': 'User Created', 'result': serializer.data}
        return Response(response, status=status.HTTP_200_OK)
