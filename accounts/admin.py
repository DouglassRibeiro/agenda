from django.contrib import admin
from .models import User, Paciente, Profissional # 1. Importe os modelos

# 2. Registre cada um deles
admin.site.register(User)
admin.site.register(Paciente)
admin.site.register(Profissional)