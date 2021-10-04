from django.contrib import admin

#importo mis modelos marca y producto
from .models import Marca, Producto

# Register your models here.

admin.site.register(Marca)
admin.site.register(Producto)
