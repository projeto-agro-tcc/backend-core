from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from estacoes.api.viewsets import EstacoesViewSet
from utils.CustomAuthToken import *

from empresas.api.viewsets import EmpresasViewSet
from usuarios.api.viewsets import UsuariosViewSet

router = routers.DefaultRouter()
router.register('empresas', EmpresasViewSet, basename='Empresas')
router.register('usuarios', UsuariosViewSet, basename='Usuarios')
router.register('estacoes', EstacoesViewSet, basename='Estacoes')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('auth/', CustomAuthToken.as_view())
]
