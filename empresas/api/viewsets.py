from rest_framework.viewsets import ModelViewSet
from empresas.models import Empresa
from .serializers import EmpresaSerializer


class EmpresasViewSet(ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer
