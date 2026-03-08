from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import MyUser
from .forms import MyUserCreationForm, MyUserChangeForm

class MyUserAdmin(UserAdmin):
    add_form = MyUserCreationForm
    form = MyUserChangeForm

    model = MyUser
    list_display = ('email', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    search_fields = ('email',)
    ordering = ('email',)

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Informações Pessoais', {'fields': ('first_name', 'last_name')}),
        ('Permissões', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
        ('Datas importantes', {'fields': ('last_login',)}),
        ('Cargo e Funções', {'fields': ('role',)}),
    )

    add_fieldsets = (
        (None, {
        'classes' : ('wide',),
        'fields': ('email', 'role', 'password', 'first_name', 'last_name')
        }),
    )

admin.site.register(MyUser, MyUserAdmin)