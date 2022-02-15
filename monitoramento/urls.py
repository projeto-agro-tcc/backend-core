from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import routers, permissions

from emw.api.viewsets import EmwViewSet
from estacoes.api.viewsets import EstacoesViewSet
from utils.CustomAuthToken import *

from empresas.api.viewsets import EmpresasViewSet
from usuarios.api.viewsets import UsuariosViewSet

schema_view = get_schema_view(
   openapi.Info(
      title="Core API",
      default_version='v1',
      description="Aplicação Core Monitoramento",
      terms_of_service="https://www.google.com/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

router = routers.DefaultRouter()
router.register('empresas', EmpresasViewSet, basename='Empresas')
router.register('usuarios', UsuariosViewSet, basename='Usuarios')
router.register('estacoes', EstacoesViewSet, basename='Estacoes')
router.register('emw', EmwViewSet, basename='Emw')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('auth/', CustomAuthToken.as_view()),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
