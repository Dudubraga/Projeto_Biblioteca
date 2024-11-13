from django.shortcuts import render, redirect
from .models import Usuario, Livro

#parte de usuarios não logados
def home(request):
    livros = Livro.objects.all()[:3]  #pegando os 3 primeiros livros
    return render(request, 'biblioteca/home.html', {'livros': livros})

def detalhes_livro(request, livro_id):
    livro = Livro.objects.get(id_livro=livro_id)
    return render(request, 'biblioteca/detalhes_livro.html', {'livro': livro})



#login e cadastro
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



#parte de usuarios logados
def usuario(request):
    # pega o ID do usuário da sessão
    
    usuario_id = request.session.get('usuario_id')
    
    if usuario_id:
        livros = Livro.objects.all() 
        usuario = Usuario.objects.get(id_usuario=usuario_id)
        return render(request, 'usuarios/homeusuario.html', {'usuario': usuario, 'livros': livros})
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
    

def detalhes_livro_usuario(request, livro_id):
    usuario_id = request.session.get('usuario_id')  
    usuario = Usuario.objects.get(id_usuario=usuario_id)
    livro = Livro.objects.get(id_livro=livro_id)
    return render(request, 'usuarios/detalhes_livro_usuario.html', {'usuario': usuario, 'livro': livro})
