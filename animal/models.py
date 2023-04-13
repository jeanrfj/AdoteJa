from django.db import models
from django.db import models
from PIL import Image
import os
from django.conf import settings
from django.utils.text import slugify
from django import forms
from contatos.models import Contato


class Animal(models.Model):
    nome_animal = models.CharField(max_length=255)
    especie = models.CharField(max_length=50,
                               default='',
                               choices=(('C', 'Cacharro'),
                                        ('G', 'Gato'),
                                        ('', ''),))
    slug = models.SlugField(unique=True, blank=True, null=True)
    raca = models.CharField(max_length=50)
    imagem = models.ImageField(
        upload_to='animal_imagens/%Y/%m', blank=True, null=True)
    data_nascimento = models.DateField()
    castrado = models.CharField(default='',
                                max_length=3,
                                choices=(('S', 'Sim'),
                                         ('N', 'Não'),
                                         ('', 'Escolha'),))
    peso = models.FloatField()
    sexo = models.CharField(default='',
                            max_length=3,
                            choices=(('M', 'Macho'),
                                     ('F', 'Fêmea'),
                                     ('', 'Escolha'),))
    cor = models.CharField(max_length=255)
    descricao = models.CharField(max_length=255)
    porte = models.CharField(max_length=7,
                             default='',
                             choices=(('P', 'Pequeno'),
                                      ('M', 'Medio'),
                                      ('G', 'Grande'),
                                      ('', 'Escolha'),))
    # TODO:VARIAVEL TEMPORARIA, FALTA DEFINIR COMO ACESSAR A OUTRA CLASSE COM AS FOTOS

    @staticmethod  # TODO: REDIMENCIONA IMAGENS ADICIONADAS
    def resize_image(img, new_width=800):
        img_full_path = os.path.join(settings.MEDIA_ROOT, img.name)
        img_pil = Image.open(img_full_path)
        original_width, original_height = img_pil.size

        print(f'width: {original_width} , height: {original_height}')

        if original_width <= new_width:
            print('largura original menor que a nova largura')
            img_pil.close()
            return

        new_height = round((new_width*original_height)/original_width)
        new_img = img_pil.resize((new_width, new_height), Image.LANCZOS)
        new_img.save(
            img_full_path,
            optimize=True,
            quality=50
        )
        print('Imagem foi redimencionada com Sucesso!')

    def save(self, *args, **kwargs):
        if not self.slug:  # AUTOMATIZA A CRIAÇÃO DE SLUG NO CADASTRO
            slug = f'{slugify(self.nome_animal)}'
            self.slug = slug

        super().save(*args, **kwargs)

        max_image_size = 800
        if self.imagem:
            self.resize_image(self.imagem, max_image_size)

    def __str__(self):
        return self.nome_animal

    class Meta:
        verbose_name = 'Animal'
        verbose_name_plural = 'Animais'


class Foto(models.Model):

    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    # foto=models.ImageField(upload_to='animal_imagens/%Y/%m',blank=True,null=True)
    nome_foto = models.CharField(max_length=255, blank=True, null=True)
    url = models.CharField(max_length=2000, blank=True, null=True)
    data_criacao = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nome_foto or self.animal.nome_animal


class FormContato(forms.ModelForm):
    class Meta:
        model = Contato
        exclude = ('mostrar','categoria',)

