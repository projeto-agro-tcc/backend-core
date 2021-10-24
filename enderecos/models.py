from django.db import models


class Endereco(models.Model):
    logradouro = models.CharField(max_length=150, null=False)
    numero = models.CharField(max_length=10, null=False)
    complemento = models.CharField(max_length=50, null=False)
    bairro = models.CharField(max_length=100, null=False)
    cidade = models.CharField(max_length=100, null=False)
    cep = models.CharField(max_length=8, null=False)
    uf = models.CharField(max_length=2, null=False)

    class Meta:
        db_table = "en_enderecos"

    def __str__(self):
        return self.logradouro
