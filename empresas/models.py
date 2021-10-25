from django.db import models
from enderecos.models import Endereco
from telefones.models import Telefone


class Empresa(models.Model):
    nome = models.CharField(max_length=150)
    cnpj = models.CharField(max_length=18)
    email = models.EmailField(null=True)
    web_site = models.CharField(max_length=200)
    endereco = models.OneToOneField(Endereco, on_delete=models.CASCADE, null=False)
    telefone = models.OneToOneField(Telefone, on_delete=models.CASCADE, null=False)
    status = models.IntegerField(default=1)

    class Meta:
        db_table = "en_empresas"

    def __str__(self):
        return self.nome
