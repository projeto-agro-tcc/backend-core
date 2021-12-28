# Generated by Django 3.2.8 on 2021-12-09 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TokenApiExterna',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_api', models.CharField(max_length=200)),
                ('token', models.CharField(max_length=512)),
            ],
            options={
                'db_table': 'en_token_api_externa',
            },
        ),
    ]