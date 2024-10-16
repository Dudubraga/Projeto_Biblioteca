from django.urls import path
from app_biblioteca import views

urlpatterns = [
    path('', views.home, name='home')
]
