from django.contrib import admin
from .models import Producto, Caracteristica

# Para administrar los modelos desde el admin de Django
admin.site.register(Producto)
admin.site.register(Caracteristica)