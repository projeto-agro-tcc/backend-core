from django.db import models

class Previsao(models.Model):
    sn_est = models.CharField(max_length=150)
    temp = models.FloatField()

    class Meta:
        db_table = "en_previsao"

    def __str__(self):
        return self.sn_est