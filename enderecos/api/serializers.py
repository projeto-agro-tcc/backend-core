from rest_framework.serializers import ModelSerializer
from enderecos.models import Endereco


class EnderecoSerializer(ModelSerializer):

    class Meta:
        model = Endereco
        fields = ('id', 'logradouro', 'numero', 'complemento', 'bairro', 'cep', 'cidade', 'uf')
