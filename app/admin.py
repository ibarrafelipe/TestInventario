from django.contrib import admin

#importo mis modelos marca y producto
from .models import Marca, Producto

# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ["nombre", "precio", "nuevo", "marca"]
    list_editable = ["precio"]
    search_fields = ["nombre"]
    list_filter = ["marca", "nuevo"]



admin.site.register(Marca)
admin.site.register(Producto, ProductoAdmin)
