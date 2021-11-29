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
    empresas = models.ManyToManyField(Empresa, blank=True, null=True, related_name='usuario')

    class Meta:
        db_table = "en_usuarios"

    def __str__(self):
        return self.username
