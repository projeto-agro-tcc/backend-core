from rest_framework.serializers import ModelSerializer
from cultivos.models import Cultivo


class CultivoSerializer(ModelSerializer):

    class Meta:
        model = Cultivo
        fields = ('id', 'nome', 'area_cultivo')
