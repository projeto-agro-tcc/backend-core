from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer
from empresas.api.serializers import EmpresaDtoSerializer
from enderecos.api.serializers import EnderecoSerializer
from telefones.api.serializers import TelefoneSerializer
from usuarios.models import Usuario


class CurrentUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'id')


class UsuarioSerializer(ModelSerializer):

    empresas = EmpresaDtoSerializer(many=True)
    endereco = EnderecoSerializer()
    telefone = TelefoneSerializer()
    user = CurrentUserSerializer()

    class Meta:
        model = Usuario
        fields = ('id', 'user', 'cpf', 'endereco', 'telefone', 'empresas')
