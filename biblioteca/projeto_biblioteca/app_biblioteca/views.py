from django.shortcuts import render, redirect
from .models import Usuario

def home(request):
    return render(request, 'biblioteca/home.html')

def cadastro(request):
    if request.method == 'POST':

        email=request.POST.get('email')
        usuario = Usuario.objects.filter(email=email).first()
        if usuario:
            return render(request, 'usuarios/cadastro.html', {'error': 'Email já cadastrado.'})
        else:
            Usuario.objects.create(
                nome=request.POST.get('nome'),
                nascimento=request.POST.get('nascimento'),
                senha=request.POST.get('senha')
            )
        return redirect('aba_login')
    return render(request, 'usuarios/cadastro.html')

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        usuario = Usuario.objects.filter(email=email).first()
        if usuario and usuario.senha == senha:
            print("Login efetuado")
            return redirect('aba_usuario')
        else:
            return render(request ,'usuarios/login.html', {'error': 'Email ou senha incorretos.'})

    return render(request, 'usuarios/login.html')

def usuario(request):
    return render(request,'usuarios/homeusuario.html')

def perfil(request):
    return render(request, 'usuarios/perfil.html')