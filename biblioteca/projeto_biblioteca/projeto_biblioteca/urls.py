from django.urls import path
from app_biblioteca import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cadastro/', views.cadastro, name='aba_cadastro'),
    path('login/', views.login, name='aba_login'),
]
