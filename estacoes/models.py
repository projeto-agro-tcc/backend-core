from django.db import models
from empresas.models import Empresa


class Estacao(models.Model):
    latitude = models.IntegerField()
    longitude = models.IntegerField()
    serial_number = models.CharField(max_length=100, unique=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, blank=True, related_name='estacoes')

    class Meta:
        db_table = "en_estacoes"

    def __str__(self):
        return self.serial_number
