from django.db import models
from empresas.models import Empresa


class EstacaoModelo(models.Model):
    code = models.CharField(max_length=50, unique=True, primary_key=True)
    city = models.CharField(max_length=100)
    latlong = models.CharField(max_length=50)
    state = models.CharField(max_length=50)

    class Meta:
        db_table = "en_estacoes_modelo"

    def __str__(self):
        return self.code


class Estacao(models.Model):
    latitude = models.IntegerField()
    longitude = models.IntegerField()
    serial_number = models.CharField(max_length=100, unique=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, blank=True, related_name='estacoes')
    estacao_modelo = models.ForeignKey(EstacaoModelo, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        db_table = "en_estacoes"

    def __str__(self):
        return self.serial_number
