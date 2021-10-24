from rest_framework.viewsets import ModelViewSet
from cultivos.api.serializers import CultivoSerializer
from cultivos.models import Cultivo


class CultivosViewSet(ModelViewSet):
    queryset = Cultivo.objects.all()
    serializer_class = CultivoSerializer
