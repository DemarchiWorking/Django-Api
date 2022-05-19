from django.db import models


class Categoria(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=500)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=50)
    preco = models.FloatField()
    descricao = models.CharField(max_length=500)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    data_criacao = models.DateField()
    def __str__(self):
        return self.nome

