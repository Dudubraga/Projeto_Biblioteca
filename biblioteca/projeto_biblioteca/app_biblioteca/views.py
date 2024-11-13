from django.shortcuts import render, redirect
from .models import Usuario

def home(request):
    return render(request, 'biblioteca/home.html')

def cadastro(request):
    if request.method == 'POST':

        email = request.POST.get('email')
        usuario = Usuario.objects.filter(email=email).first()

        if usuario:
            return render(request, 'usuarios/cadastro.html', {'error': 'Email já cadastrado.'})
        else:
            Usuario.objects.create(
                nome=request.POST.get('nome'),
                email=email,
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
            request.session['usuario_id'] = usuario.id_usuario #salva o id do usuario na sessão
            return redirect('aba_usuario')
        else:
            return render(request ,'usuarios/login.html', {'error': 'Email ou senha incorretos.'})

    return render(request, 'usuarios/login.html')

def usuario(request):
    # pega o ID do usuário da sessão
    usuario_id = request.session.get('usuario_id')
    
    if usuario_id:
        usuario = Usuario.objects.get(id_usuario=usuario_id)
        return render(request, 'usuarios/homeusuario.html', {'usuario': usuario})
    else:
        # se não tiver logado, redireciona para o login mesmo ele checando antes
        return redirect('aba_login')

def perfil(request):
    usuario_id = request.session.get('usuario_id')
    
    if usuario_id:
        usuario = Usuario.objects.get(id_usuario=usuario_id)
        return render(request, 'usuarios/perfil.html', {'usuario': usuario})
    else:
        return redirect('aba_login')