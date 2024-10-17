from django.shortcuts import render

def home(request):
    return render(request,'biblioteca/home.html')

def cadastro(request):
    return render(request,'biblioteca/cadastro.html')
