# Generated by Django 4.1.7 on 2023-03-19 22:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_animal', models.CharField(max_length=255)),
                ('especie', models.CharField(max_length=255)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('raca', models.CharField(max_length=50)),
                ('data_nascimento', models.DateField()),
                ('castrado', models.CharField(choices=[('S', 'Sim'), ('N', 'Não'), ('', 'Escolha')], default='', max_length=3)),
                ('peso', models.FloatField()),
                ('sexo', models.CharField(choices=[('F', 'Femea'), ('M', 'Macho'), ('', 'Escolha')], default='', max_length=3)),
                ('cor', models.CharField(max_length=255)),
                ('descricao', models.CharField(max_length=255)),
                ('porte', models.CharField(choices=[('P', 'Pequeno'), ('M', 'Medio'), ('G', 'Grande'), ('', 'Escolha')], default='', max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='Foto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.ImageField(blank=True, null=True, upload_to='animal_imagens/%Y/%m')),
                ('url', models.CharField(max_length=2000)),
                ('data_criacao', models.DateField()),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animal.animal')),
            ],
        ),
    ]