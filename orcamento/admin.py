from django.contrib import admin
from .models import *

@admin.register(usuario)
class usuarioAdmn(admin.ModelAdmin):
    list_display = ['nome', 'sobre_nome', 'receita', 'ativo']
    list_edit = ['ativo']