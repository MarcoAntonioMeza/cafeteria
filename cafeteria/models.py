from django.db import models
from customerUser.models import CustomUser

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='productos/')
    status = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

class SolicitudProducto(models.Model):
    nombre_cliente = models.CharField(max_length=200)
    cantidad = models.IntegerField(default=1)
    mensaje = models.TextField(blank=True, null=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    
    status = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Solicitud de {self.nombre_cliente} para {self.producto.nombre}"
    
    def total(self):
        return self.cantidad * self.producto.precio
