# Generated by Django 3.2.8 on 2021-10-23 02:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('telefones', '0001_initial'),
        ('enderecos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('cnpj', models.CharField(max_length=18)),
                ('web_site', models.CharField(max_length=200)),
                ('endereco', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='enderecos.endereco')),
                ('telefone', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='telefones.telefone')),
            ],
            options={
                'db_table': 'en_empresas',
            },
        ),
    ]
