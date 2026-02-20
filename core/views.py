from django.shortcuts import render

def core_view(request):
    return render(request,'core/index.html')

def teste_htmx(request):
    return render (request,'core/partials/menssagem.html')