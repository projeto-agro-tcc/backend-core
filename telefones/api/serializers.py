from rest_framework.serializers import ModelSerializer
from telefones.models import Telefone


class TelefoneSerializer(ModelSerializer):

    class Meta:
        model = Telefone
        fields = ('id', 'residencial', 'celular', 'outro')
