from django.contrib.auth.models import User
from django.db import models
from empresas.models import Empresa
from enderecos.models import Endereco
from telefones.models import Telefone


class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cpf = models.CharField(max_length=11, unique=True)
    status = models.IntegerField()
    endereco = models.OneToOneField(Endereco, on_delete=models.CASCADE, null=False)
    telefone = models.OneToOneField(Telefone, on_delete=models.CASCADE, null=False, unique=True)
    empresas = models.ManyToManyField(Empresa)

    class Meta:
        db_table = "en_usuarios"

    def __str__(self):
        return self.user.username
