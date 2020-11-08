from django.db import models
from django.contrib.auth.forms import User
# Create your models here.

class Atleta(models.Model):
    Id_Atleta=models.AutoField(primary_key=True)
    username=models.OneToOneField(User,on_delete=models.CASCADE)
    Num_Matri=models.CharField(max_length=20,verbose_name="Numero Matricula",blank=True,null=True)
    Nom=models.CharField(max_length=30,verbose_name="Nombre")
    Ape=models.CharField(max_length=60,verbose_name="Apellidos") 
    Dire=models.CharField(max_length=60,verbose_name="Direccion",)
    Pobla=models.CharField(max_length=50,verbose_name="Poblacion")
    Cod_Pos=models.CharField(max_length=5,verbose_name="Cod. Postal")
    Tel=models.CharField(max_length=9,verbose_name="Telefono")
    Fecha_Nac=models.DateField(verbose_name="Fecha Nacimiento")
    email=models.EmailField( max_length=40,verbose_name="E-mail")

    def __str__(self):
        return self.Nom


    
    
class Prueba(models.Model):
    Id_Prueba=models.AutoField(primary_key=True)
    Nom_Prueba=models.CharField(max_length=50,verbose_name="Nom. Prueba")
    Localidad=models.CharField(max_length=50,verbose_name="Localidad")
    Fecha_Pr=models.DateField(verbose_name="Fecha")
    Fecha_Inicio=models.DateField(verbose_name="Inscripcion Desde")
    Fecha_Fin=models.DateField(verbose_name="Inscripcion Hasta")

    def __str__(self):
        return self.Nom_Prueba

    

class Categoria(models.Model):
    Id_Cat=models.AutoField(primary_key=True)
    Id_Prueba=models.ForeignKey(Prueba,on_delete=models.CASCADE)
    Modalidad=models.CharField(max_length=50)
    
    def __str__(self):
        return self.Modalidad

    

class Inscripcion(models.Model):
    Id_Ins=models.AutoField(primary_key=True)
    username=models.ForeignKey(User,on_delete=models.CASCADE)
    Id_Cat=models.ForeignKey(Categoria,on_delete=models.CASCADE)
    Id_Prueba=models.ForeignKey(Prueba,on_delete=models.CASCADE)
