from rest_framework.serializers import ModelSerializer
from estacoes.models import Estacao


class EstacaoSerializer(ModelSerializer):

    class Meta:
        model = Estacao
        fields = ('id', 'latitude', 'longitude', 'serial_number')
