from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import CustomUserCreationForm

def register_view(request):
    form = CustomUserCreationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('core:agenda_view')
    
    # Se for HTMX, retorna apenas o formulário (partial)
    if request.headers.get('HX-Request'):
        return render(request, 'accounts/partials/register_form.html', {'form': form})
        
    return render(request, 'accounts/register.html', {'form': form})

def teste_view(request):
    return  render(request, 'accounts/teste.html')