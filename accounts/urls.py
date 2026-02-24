from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.accounts_login, name='login.urls'),
    path('register/', views.accounts_register, name='login.urls'),
]