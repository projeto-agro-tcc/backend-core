# Generated by Django 3.2.8 on 2021-10-23 02:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('telefones', '0001_initial'),
        ('enderecos', '0001_initial'),
        ('usuarios', '0002_alter_usuario_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='endereco',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='enderecos.endereco'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='telefone',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='telefones.telefone'),
        ),
    ]