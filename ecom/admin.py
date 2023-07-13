from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Produtos


class ProdutosAdmin(admin.ModelAdmin):
    fields = ['nome', 'preco', 'estoque', 'valor', 'imagem']

admin.site.register(Produtos, ProdutosAdmin)