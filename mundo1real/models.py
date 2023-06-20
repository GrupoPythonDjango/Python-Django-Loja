from django.db import models

# Create your models here.


class Usuario(models.Model):
    email = models.EmailField(unique=True)
    nome = models.CharField(max_length=100)
    senha = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.nome
    

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    setor = models.CharField(max_length=100)
    valor = models.IntegerField(100)
    ativo = models.BooleanField(default=False)