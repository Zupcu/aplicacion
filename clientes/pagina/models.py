from django.db import models
from django.contrib.auth.models import AbstractUser

# Modelo de usuario con perfiles
class Usuario(AbstractUser):
    ADMIN = 'admin'
    USER = 'user'
    ROLE_CHOICES = [
        (ADMIN, 'Administrador'),
        (USER, 'Usuario'),
    ]
    role = models.CharField(max_length=5, choices=ROLE_CHOICES, default=USER)

# Modelo de cliente
class Cliente(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20)
    direccion = models.TextField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


