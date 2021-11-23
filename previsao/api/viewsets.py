from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from utils.permissions.permissions import authenticated_user, allowed_users_by_group
from previsao.models import Previsao

class PrevisaoViewSet(ModelViewSet):

    #@authenticated_user
    #@allowed_users_by_group(allowed_roles=['admin', 'super_user'])
    def list(self, request, *args, **kwargs):
        #query = Previsao.objects.all()
        query = Previsao.objects.filter(sn_est='A001')
        print(query)
        return Response(query)