from django.urls import path
from app_biblioteca import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cadastro/', views.cadastro, name='aba_cadastro'),
    path('login/', views.login, name='aba_login'),
    path('usuario/', views.usuario, name='aba_usuario'),
    path('perfil/', views.perfil, name='aba_perfil'),
    path('livro/<int:livro_id>/', views.detalhes_livro, name='detalhes_livro'),
    path('usuario/livro/<int:livro_id>/', views.detalhes_livro_usuario, name='detalhes_livro_usuario'),
]
