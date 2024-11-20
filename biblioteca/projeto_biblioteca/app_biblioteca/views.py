from django.shortcuts import redirect, get_object_or_404, render
from django.contrib import messages
from .models import Livro, Usuario, Comentario # Removido BibliotecaUsuario e adicionado Usuario

#parte de usuarios não logados
def home(request):
    livros = Livro.objects.all()[:3]  #pegando os 3 primeiros livros
    return render(request, 'biblioteca/home.html', {'livros': livros})

def detalhes_livro(request, livro_id):
    livro = Livro.objects.get(id_livro=livro_id)
    comentarios = Comentario.objects.filter(livro=livro_id)
    return render(request, 'biblioteca/detalhes_livro.html', {'livro': livro, 'comentarios': comentarios})



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
    if not usuario_id:
        return redirect('aba_login')
        
    usuario = Usuario.objects.get(id_usuario=usuario_id)
    livro = Livro.objects.get(id_livro=livro_id)
    comentarios = Comentario.objects.filter(livro=livro_id)
    

    livro_favoritado = usuario.favoritos.filter(id_livro=livro_id).exists()
    livro_lido = usuario.lidos.filter(id_livro=livro_id).exists()
    livro_proxima_leitura = usuario.proximas_leituras.filter(id_livro=livro_id).exists()
    
    context = {
        'usuario': usuario,
        'livro': livro,
        'comentarios': comentarios,
        'livro_favoritado': livro_favoritado,
        'livro_lido': livro_lido,
        'livro_proxima_leitura': livro_proxima_leitura
    }
    
    return render(request, 'usuarios/detalhes_livro_usuario.html', context)


def adicionar_favorito(request, id_livro):
    usuario_id = request.session.get('usuario_id')
    if not usuario_id:
        return redirect('aba_login')
        
    usuario = Usuario.objects.get(id_usuario=usuario_id)
    livro = Livro.objects.get(id_livro=id_livro)
    
    if usuario.favoritos.filter(id_livro=id_livro).exists():
        usuario.favoritos.remove(livro)
    else:
        usuario.favoritos.add(livro)
    
    return redirect('detalhes_livro_usuario', livro_id=id_livro)

def adicionar_lido(request, id_livro):
    usuario_id = request.session.get('usuario_id')
    if not usuario_id:
        return redirect('aba_login')
        
    usuario = Usuario.objects.get(id_usuario=usuario_id)
    livro = Livro.objects.get(id_livro=id_livro)
    
    if usuario.lidos.filter(id_livro=id_livro).exists():
        usuario.lidos.remove(livro)
    else:
        usuario.lidos.add(livro)
    
    return redirect('detalhes_livro_usuario', livro_id=id_livro)

def adicionar_proxima_leitura(request, id_livro):
    usuario_id = request.session.get('usuario_id')
    if not usuario_id:
        return redirect('aba_login')
        
    usuario = Usuario.objects.get(id_usuario=usuario_id)
    livro = Livro.objects.get(id_livro=id_livro)
    
    if usuario.proximas_leituras.filter(id_livro=id_livro).exists():
        usuario.proximas_leituras.remove(livro)
    else:
        usuario.proximas_leituras.add(livro)
    
    return redirect('detalhes_livro_usuario', livro_id=id_livro)


def favoritos(request):
    usuario_id = request.session.get('usuario_id')
    usuario = Usuario.objects.get(id_usuario=usuario_id)
    livros_fav = usuario.favoritos.all()
    return render(request,'usuarios/favoritos.html',{'usuario': usuario,'livros_fav' : livros_fav})
    
def lidos_e_proxLeitura(request):
    usuario_id = request.session.get('usuario_id')
    usuario = Usuario.objects.get(id_usuario=usuario_id)
    livros_lidos = usuario.lidos.all()
    livros_prox_leitura = usuario.proximas_leituras.all()
    return render(request,'usuarios/lidos_prox_leituras.html',{'usuario': usuario,'livros_lidos' : livros_lidos, 'livros_prox_leitura' : livros_prox_leitura})

def comentar(request, id_livro):
    livro = get_object_or_404(Livro, id_livro=id_livro)
    usuario_id = request.session.get('usuario_id')
    if usuario_id:
        if request.method == 'POST':
            texto = request.POST.get('comentario')
            if texto:
                usuario = Usuario.objects.get(id_usuario=usuario_id)
                Comentario.objects.create(
                    usuario=usuario,
                    livro=livro,
                    texto=texto
                )
                return redirect('detalhes_livro_usuario', livro_id=id_livro)
        
        return render(request, 'usuarios/comentar.html', {'livro': livro})
    return redirect('aba_login')