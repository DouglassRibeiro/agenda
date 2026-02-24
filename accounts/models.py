from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager, Group



class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('O usuário precisa de um email válido')
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)
    
    


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    nome_completo = models.CharField(max_length=255)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = ['email'] 
    REQUIRED_FIELDS = ['nome_completo']

    def __str__(self):
        return self.email

class User(AbstractBaseUser):
    email = models.EmailField(unique=True, max_length=255)
    nome_completo = models.CharField(max_length=255)
    telefone = models.CharField(max_length=20)
    is_active = models.BooleanField(max_length=True)
    is_admin = models.BooleanField(max_length=False)
    
    USERNAME_FILD = ['email']
    
    REQUIRED_FIELDS = ['nome_completo']
    
    def __str__(self):
        return self.email
