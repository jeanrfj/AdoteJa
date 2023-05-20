# Generated by Django 4.2 on 2023-05-20 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animal', '0008_animal_ativo'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='status_adocao_animal',
            field=models.CharField(choices=[('A', 'Para Adocao'), ('P', 'Pausado'), ('AD', 'Adotado'), ('', '')], default='A', max_length=255, verbose_name='Status de Adoção do Animal'),
        ),
    ]
