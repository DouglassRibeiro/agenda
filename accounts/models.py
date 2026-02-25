from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager, Group



class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('O usuário precisa de um email válido')
        tipo = extra_fields.pop('tipo_perfil', None)
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        
        if tipo:
            grupo = Group.objects.filter(name=tipo).first()
            if grupo:
                user.groups.add(grupo)
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)
    
class User(AbstractBaseUser, PermissionsMixin):
    
    TIPOS_USUARIO = (
        ('paciente', 'Paciente'),
        ('profissional', 'Profissional'),
        ('administraca', 'Recepcionista'),
    )
    
    email = models.EmailField(unique=True)
    nome_completo = models.CharField(max_length=255)
    telefone = models.CharField(max_length=20, blank=True, null=True)

    tipo = models.CharField(max_length=20, choices=TIPOS_USUARIO, default='paciente')
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email' 
    REQUIRED_FIELDS = ['nome_completo']

    def __str__(self):
        return self.email
    pass

class Paciente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    data_nascimento = models.DateField(null=True, blank=True)
    cpf = models.CharField(max_length=14)

    def __str__(self):
        return f"Paciente: {self.user.nome_completo}"

class Profissional(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    registro_conselho = models.CharField(max_length=30)
    especialidade = models.CharField(max_length=100)

    def __str__(self):
        return f"Profissional: {self.user.nome_completo}"