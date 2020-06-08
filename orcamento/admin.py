from django.contrib import admin
from .models import *

@admin.register(usuarios)
class usuarioAdmn(admin.ModelAdmin):
    list_display = ['nome', 'sobre_nome', 'receita', 'ativo']
    list_edit = ['ativo']


@admin.register(categorias)
class categoriaAdmin(admin.ModelAdmin):
    list_display = ['categoria', 'ativo']
    list_edit = ['ativo']   

@admin.register(despesas)
class despesasAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'categoria', 'descricao', 'valor', 'data']
    list_edit = ['valor']  
    list_filter = ['categoria', 'usuario']