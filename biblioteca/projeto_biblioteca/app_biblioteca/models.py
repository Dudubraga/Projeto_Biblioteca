from django.db import models

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.TextField(max_length  = 255)    
    nascimento = models.DateField()
    email = models.EmailField()
    senha = models.TextField(max_length=255)   
