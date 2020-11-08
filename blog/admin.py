from django.contrib import admin
from .models import Categoria,Post

# Register your models here.

class CategoriaAdm(admin.ModelAdmin):
    readonly_fields=('created','updated')


class PostAdm(admin.ModelAdmin):
    readonly_fields=('created','updated')


admin.site.register(Categoria,CategoriaAdm)
admin.site.register(Post,PostAdm)



