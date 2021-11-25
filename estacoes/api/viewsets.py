from rest_framework.authentication import TokenAuthentication
from rest_framework.viewsets import ModelViewSet
from estacoes.api.serializers import EstacaoSerializer
from estacoes.models import Estacao


class EstacoesViewSet(ModelViewSet):
    queryset = Estacao.objects.all()
    serializer_class = EstacaoSerializer
    authentication_classes = (TokenAuthentication,)
