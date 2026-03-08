from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import MyUser

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ('email','role')
        
class MyUserChangeForm(UserChangeForm):
    class Meta:
        model = MyUser
        fields = ('email', 'is_active', 'is_staff', 'is_superuser')