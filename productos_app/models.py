from django.db import models

# Modelo principal del proyecto
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=300)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre
    
# Modelo adicional del proyecto
class Caracteristica(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='caracteristica')
    nombre = models.CharField(max_length=100)
    valor = models.CharField(max_length=300)

    def __str__(self):
        return f"{self.nombre}: {self.valor}"