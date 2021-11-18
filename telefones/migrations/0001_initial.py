# Generated by Django 3.2.8 on 2021-10-25 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Telefone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('residencial', models.CharField(blank=True, max_length=14, null=True, unique=True)),
                ('celular', models.CharField(max_length=12, unique=True)),
                ('outro', models.CharField(blank=True, max_length=14, null=True, unique=True)),
            ],
            options={
                'db_table': 'en_telefones',
            },
        ),
    ]