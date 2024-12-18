from django.urls import path
from app_biblioteca import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cadastro/', views.cadastro, name='aba_cadastro'),
    path('login/', views.login, name='aba_login'),
    path('usuario/', views.usuario, name='aba_usuario'),
    path('perfil/', views.perfil, name='aba_perfil'),
    path('buscar/', views.buscar_livro, name='buscar_livro'),
    path('usuario/buscar/', views.buscar_livro_usuario, name='buscar_livro_usuario'),
    path('livro/<int:livro_id>/', views.detalhes_livro, name='detalhes_livro'),
    path('usuario/livro/<int:livro_id>/', views.detalhes_livro_usuario, name='detalhes_livro_usuario'),
    path('livro/<int:id_livro>/adicionar-favorito/', views.adicionar_favorito, name='adicionar_favorito'),
    path('livro/<int:id_livro>/adicionar-lido/', views.adicionar_lido, name='adicionar_lido'),
    path('livro/<int:id_livro>/adicionar-proxima-leitura/', views.adicionar_proxima_leitura, name='adicionar_proxima_leitura'),
    path('favoritos/', views.favoritos, name='favoritos'),
    path('lidos_e_proxLeitura/', views.lidos_e_proxLeitura, name='lidos_e_proxLeitura'),
    path('livros/comentario/<int:id_livro>/', views.comentar, name='comentar'),
    
    ]
