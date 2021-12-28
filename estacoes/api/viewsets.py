import requests
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from estacoes.api.serializers import EstacaoSerializer
from estacoes.models import Estacao


class EstacoesViewSet(ModelViewSet):
    queryset = Estacao.objects.all()
    serializer_class = EstacaoSerializer()
    authentication_classes = (TokenAuthentication,)

    def list(self, request, *args, **kwargs):
        queryset = Estacao.objects.all()
        serializer = EstacaoSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['GET'])
    def get_data(self, request):
        response = requests.get("http://127.0.0.1:7000/endpoints/get_data/")
        response = {'response': response}
        return Response(response, status=status.HTTP_200_OK)
