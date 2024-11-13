from django.db import models

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.TextField(max_length  = 255)    
    nascimento = models.DateField()
    email = models.EmailField()
    senha = models.TextField(max_length=255)   

class Livro(models.Model):
    id_livro = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    descricao = models.TextField()
    ano_publicacao = models.IntegerField()
    imagem_url = models.URLField(max_length=255, null=True, blank=True)

   