from django.contrib import admin
from inicio.models import Empleado
from .models import DatosExtras

# Register your models here.

@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'documento', 'fecha_ingreso', 'localidad', 'informacion')
    search_fields = ('nombre', 'apellido', 'documento')




admin.site.register(DatosExtras)