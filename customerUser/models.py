# models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Campos adicionales
    direccion = models.CharField(max_length=255, blank=True, null=True)
    foto_perfil = models.ImageField(upload_to='foto_perfil/', blank=True, null=True)

    def __str__(self):
        return self.username
