from rest_framework.serializers import ModelSerializer
from cultivos.api.serializers import CultivoSerializer
from empresas.models import Empresa
from enderecos.api.serializers import EnderecoSerializer
from estacoes.api.serializers import EstacaoSerializer
from telefones.api.serializers import TelefoneSerializer


class EmpresaSerializer(ModelSerializer):

    cultivos = CultivoSerializer(many=True, read_only=True)
    endereco = EnderecoSerializer()
    telefone = TelefoneSerializer()
    estacoes = EstacaoSerializer(many=True, read_only=True)

    class Meta:
        model = Empresa
        fields = ('id', 'nome', 'email', 'web_site', 'cultivos', 'endereco', 'telefone', 'estacoes')


class EmpresaDtoSerializer(ModelSerializer):

    estacoes = EstacaoSerializer(many=True, read_only=True)
    cultivos = CultivoSerializer(many=True, read_only=True)

    class Meta:
        model = Empresa
        fields = ('id', 'nome', 'email', 'web_site', 'cultivos', 'estacoes')
