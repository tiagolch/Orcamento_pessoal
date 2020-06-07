from django.db import models

class usuario(models.Model):
    nome = models.CharField(max_length=20, verbose_name='Nome')
    sobre_nome = models.CharField(max_length=20, verbose_name='Sobre Nome')
    senha = models.CharField(max_length=10, verbose_name='Senha')
    receita = models.FloatField(verbose_name='Receita')
    ativo = models.BooleanField(default=True)

    class Meta:
        db_table = 'usuario'

    def __str__(self):
        return self.nome