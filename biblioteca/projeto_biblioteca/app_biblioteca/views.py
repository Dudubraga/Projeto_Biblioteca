from django.shortcuts import render
from .models import Usuario

def home(request):
    return render(request,'biblioteca/home.html')

def cadastro(request):
    return render(request,'biblioteca/cadastro.html')

def login(request):
    return render(request, 'biblioteca/login.html')

def usuarios(request):
    #salvar os dados da tela para o banco de dados
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.nascimento = request.POST.get('nascimento')
    novo_usuario.email = request.POST.get('email')
    novo_usuario.senha = request.POST.get('senha')
    novo_usuario.save()

    usuarios = {
        'usuarios': Usuario.objects.all()
    }

    return render(request, 'biblioteca/usuarios.html', usuarios)