from django.db import models


class Livros(models.Model):
    isbn = models.CharField(max_length=13)
    data_criacao = models.DateField()
    autor = models.CharField(max_length=255)
    titulo = models.CharField(max_length=255)
