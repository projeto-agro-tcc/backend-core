from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from utils.permissions.permissions import authenticated_user, allowed_users_by_group
from previsao.models import Previsao
from .serializers import PrevisaoSerializer

class PrevisaoViewSet(ModelViewSet):
    queryset = Previsao.objects.all()
    #@authenticated_user
    #@allowed_users_by_group(allowed_roles=['admin', 'super_user'])
    def list(self, request, *args, **kwargs):
        #queryset = Previsao.objects.filter(sn_est='A001')
        queryset = Previsao.objects.get(sn_est='A002')
        serializer = PrevisaoSerializer(queryset)
        print(serializer)
        return Response(serializer.data)
