from django.contrib.auth.models import AbstractUser
from django.db import models
from empresas.models import Empresa
from enderecos.models import Endereco
from telefones.models import Telefone


class Usuario(AbstractUser):
    cpf = models.CharField(max_length=11, unique=True)
    status = models.IntegerField(default=1)
    endereco = models.OneToOneField(Endereco, on_delete=models.CASCADE, null=True, blank=True)
    telefone = models.OneToOneField(Telefone, on_delete=models.CASCADE, null=True, blank=True, unique=True)
    empresas = models.ManyToManyField(Empresa, blank=True, null=True)

    class Meta:
        db_table = "en_usuarios"

    def __str__(self):
        return self.username

class TokenApiExterna(models.Model):
    nome_api = models.CharField(max_length=200)
    token = models.CharField(max_length=512)

    class Meta:
        db_table = "en_token_api_externa"

    def __str__(self):
        return self.nome_api
