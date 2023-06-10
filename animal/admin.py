from django.contrib import admin
from . import models
#from .models import Produto,Variacao
#from .models import *


class FotoInline(admin.TabularInline):
    model = models.Foto
    extra = 1
    

class AnimalAdmin(admin.ModelAdmin): #ITENS QUE VAO APARECER NO DISPLAY DO ADMIN
    #list_display=['nome','descricao_curta','get_preco_formatado','get_preco_promocional_formatado']
    inlines = [
        FotoInline
    ]

admin.site.register(models.Animal,AnimalAdmin)
admin.site.register(models.Foto)

