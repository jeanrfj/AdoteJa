# Generated by Django 4.2 on 2023-05-20 07:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('animal', '0009_animal_status_adocao_animal'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='animal',
            name='ativo',
        ),
    ]
