from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer
from empresas.api.serializers import EmpresaDtoSerializer
from enderecos.api.serializers import EnderecoSerializer
from telefones.api.serializers import TelefoneSerializer
from usuarios.api.service import UsuarioService
from usuarios.models import Usuario


class UsuarioSerializer(ModelSerializer):

    empresas = EmpresaDtoSerializer(many=True)
    endereco = EnderecoSerializer()
    telefone = TelefoneSerializer()

    class Meta:
        model = Usuario
        fields = ('id', 'username', 'first_name', 'last_name', 'cpf', 'endereco', 'telefone', 'empresas')
