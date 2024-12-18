from django.db import models

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.TextField(max_length  = 255)    
    nascimento = models.DateField()
    email = models.EmailField()
    senha = models.TextField(max_length=255)
    favoritos = models.ManyToManyField('Livro', related_name='favoritos', blank=True)
    lidos = models.ManyToManyField('Livro', related_name='lidos', blank=True)
    proximas_leituras = models.ManyToManyField('Livro', related_name='proximas_leituras', blank=True)

class Livro(models.Model):
    id_livro = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    descricao = models.TextField()
    ano_publicacao = models.IntegerField()
    imagem_url = models.URLField(max_length=255, null=True, blank=True)
    link_livro = models.URLField(max_length=255, null=True, blank=True)

class Comentario(models.Model):
    id_comentario = models.AutoField(primary_key=True)
    usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    livro = models.ForeignKey('Livro', on_delete=models.CASCADE)
    texto = models.TextField()
   