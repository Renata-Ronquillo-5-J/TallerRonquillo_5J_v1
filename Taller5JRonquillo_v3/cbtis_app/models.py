from django.db import models

# Create your models here.
class AlumnoT(models.Model):
    Apaterno=models.CharField(max_length=50,verbose_name="Apellido Paterno")
    Amaterno=models.CharField(max_length=50,verbose_name="Apellido Materno")
    Nombre=models.CharField(max_length=100,verbose_name="Nombre(s)")
    Fecha_nacimiento=models.DateField(verbose_name="Fecha de nacimiento",null=False,blank=False)
    Fecha_ingreso=models.DateField(verbose_name="Fecha de ingreso",null=False,blank=False)

