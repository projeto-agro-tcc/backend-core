from rest_framework.serializers import ModelSerializer

from estacoes.models import Estacao, EstacaoModelo


class EstacaoModeloSerializer(ModelSerializer):

    class Meta:
        Model = EstacaoModelo
        fields = ('code', 'city', 'latlong', 'state')


class EstacaoSerializer(ModelSerializer):

    estacao_modelo = EstacaoModeloSerializer

    class Meta:
        model = Estacao
        fields = ('latitude', 'longitude', 'serial_number', 'estacao_modelo')
