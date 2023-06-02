from django.db import models

# Create your models here.


class Usuario(models.Model):
    email = models.EmailField(unique=True)
    nome = models.CharField(max_length=100)
    senha = models.CharField(max_length=100)
