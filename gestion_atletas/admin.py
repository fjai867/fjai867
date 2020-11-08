from django.contrib import admin
from gestion_atletas.models import Atleta, Prueba, Categoria, Inscripcion

# Register your models here.

class AtletasAd(admin.ModelAdmin):
    list_display=("Nom","Ape","Dire")
    search_fields=("Nom","Ape")

class PruebaAd(admin.ModelAdmin):
    list_display=("Nom_Prueba", "Localidad")
    search_fields=("Nom_Prueba", "Localidad")

class CatAd(admin.ModelAdmin):
    list_display=("Id_Prueba","Modalidad")
    
    


   

admin.site.register(Atleta,AtletasAd)
admin.site.register(Prueba,PruebaAd)
admin.site.register(Categoria,CatAd)
admin.site.register(Inscripcion)