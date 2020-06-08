from django.db import models

class usuarios(models.Model):
    nome = models.CharField(max_length=20, verbose_name='Nome')
    sobre_nome = models.CharField(max_length=20, verbose_name='Sobre Nome')
    senha = models.CharField(max_length=10, verbose_name='Senha')
    receita = models.FloatField(verbose_name='Receita')
    ativo = models.BooleanField(default=True)

    class Meta:
        db_table = 'usuarios'

    def __str__(self):
        return self.nome


class categorias(models.Model):
    categoria = models.CharField(max_length=25, verbose_name='Categoria')
    ativo = models.BooleanField(default=True)

    class Meta:
        db_table = 'categorias'

    def __str__(self):
        return self.categoria



class despesas(models.Model):
    usuario = models.ForeignKey(usuarios, on_delete=models.DO_NOTHING , verbose_name='Usuario')
    categoria = models.ForeignKey(categorias, on_delete=models.DO_NOTHING, verbose_name='Categoria')
    descricao = models.CharField(max_length=100, verbose_name='Descrição')
    valor = models.FloatField(verbose_name='Valor')
    data = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'despesas'

    def __str__(self):
        return str(self.usuario)+' '+str(self.categoria)

    def get_data(self):
        return self.data.strftime('%d/%m/%Y %H:%M')

