from django.shortcuts import render

# Create your views here.

def accounts_login(request):
    return render(request, 'accounts/login.html')

def accounts_register(request):
    return render(render, 'accounts/register.html')