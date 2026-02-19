from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.core_view, name='core.urls'),
    path('teste-htmx/', views.teste_htmx, name='teste_htmx'),
]
