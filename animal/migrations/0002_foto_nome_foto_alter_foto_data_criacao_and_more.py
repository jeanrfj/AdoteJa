# Generated by Django 4.1.7 on 2023-03-19 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='foto',
            name='nome_foto',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='foto',
            name='data_criacao',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='foto',
            name='url',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
    ]