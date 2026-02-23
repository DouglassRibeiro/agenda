from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'telefone') # Seus campos personalizados

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Aplicando Tailwind em todos os campos de uma vez
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'w-full px-4 py-2 border rounded-lg focus:ring-2 focus:ring-blue-500 outline-none transition-all'
            })