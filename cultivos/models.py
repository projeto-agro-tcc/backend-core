from django.db import models
from empresas.models import Empresa


class Cultivo(models.Model):
    nome = models.CharField(max_length=100)
    area_cultivo = models.FloatField(null=True, blank=True)
    status = models.BooleanField()
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, null=False, related_name='cultivos')

    class Meta:
        db_table = "en_cultivos"

    def __str__(self):
        return self.nome
