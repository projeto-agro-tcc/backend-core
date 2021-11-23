from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from utils.CustomAuthToken import *

from empresas.api.viewsets import EmpresasViewSet
from usuarios.api.viewsets import UsuariosViewSet
from previsao.api.viewsets import PrevisaoViewSet

router = routers.DefaultRouter()
router.register('empresas', EmpresasViewSet, basename='Empresas')
router.register('usuarios', UsuariosViewSet, basename='Usuarios')
router.register('previsao', PrevisaoViewSet, basename='Previsao')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('auth/', CustomAuthToken.as_view())
]
