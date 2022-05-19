from django.contrib import admin
from djangov1.models import Categoria, Produto

class Produtos(admin.ModelAdmin):
    list_display = ('id', 'nome', 'preco', 'descricao', 'categoria', 'data_criacao')
    list_display_links = ('id', 'nome', 'preco')
    search_fields = ('nome',)
    list_per_page = 20

admin.site.register(Produto, Produtos)

class Categorias(admin.ModelAdmin):
    list_display = ('id', 'nome', 'descricao')
    list_display_links = ('id', 'nome', )
    search_fields = ('nome',)
    list_per_page = 20

admin.site.register(Categoria, Categorias)
