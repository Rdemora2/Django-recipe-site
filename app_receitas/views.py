from django.shortcuts import render

def index(request):
    return render(request, "app_receitas/index.html")

def receita(request):
    return render(request, "app_receitas/receita.html")