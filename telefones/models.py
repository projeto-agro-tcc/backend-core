from django.db import models


class Telefone(models.Model):
    residencial = models.CharField(max_length=14, null=True, blank=True, unique=True)
    celular = models.CharField(max_length=12, null=False, unique=True)
    outro = models.CharField(max_length=14, null=True, blank=True, unique=True)

    class Meta:
        db_table = "en_telefones"

    def __str__(self):
        return self.celular
