# Generated by Django 3.2.8 on 2021-10-23 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_auto_20211023_0249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='cpf',
            field=models.CharField(max_length=11, unique=True),
        ),
    ]
