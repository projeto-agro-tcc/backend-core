# Generated by Django 3.2.8 on 2021-10-24 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enderecos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='endereco',
            name='cidade',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]