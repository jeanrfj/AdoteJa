# Generated by Django 4.1.7 on 2023-03-22 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animal', '0002_foto_nome_foto_alter_foto_data_criacao_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='animal',
            options={'verbose_name': 'Animal', 'verbose_name_plural': 'Animais'},
        ),
        migrations.AlterField(
            model_name='animal',
            name='especie',
            field=models.CharField(choices=[('C', 'Cacharro'), ('G', 'Gato')], default='', max_length=7),
        ),
    ]