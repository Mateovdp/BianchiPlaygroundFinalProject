from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Empleado(models.Model):
    nombre=models.CharField(max_length=20) 
    apellido=models.CharField(max_length=20) 
    documento=models.IntegerField() 
    fecha_ingreso=models.DateField()
    localidad=models.CharField(max_length=20)
    informacion = models.CharField(max_length=500)
    avatar = models.ImageField(upload_to='imagenes_empleados', null=True, blank=True)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido} {self.fecha_ingreso}"


class DatosExtras(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatares', null=True, blank=True)
    fecha_creacion = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Datos extra del usuario {self.user}'
    
