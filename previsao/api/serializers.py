from rest_framework.serializers import ModelSerializer
from previsao.models import Previsao


class PrevisaoSerializer(ModelSerializer):

    class Meta:
        model = Previsao
        fields = ('id', 'sn_est', 'temp')
