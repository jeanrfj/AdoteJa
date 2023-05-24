# Generated by Django 4.2 on 2023-05-23 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animal', '0014_alter_animal_status_adocao_animal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='status_adocao_animal',
            field=models.CharField(choices=[('P', 'Para Adocao'), ('AD', 'Adotado'), ('', '')], default='P', max_length=255, verbose_name='Status de Adoção do Animal'),
        ),
    ]