

from django.urls import path
from blog import views



urlpatterns = [
    
    #Url imprime todos los post
    path("blog/",views.blog,name="blog"),

    #Imprime los post filtrados por categori
    path("blogfilter/<int:Id_categoria>",views.blogcategoria,name="blogfilter"),



    

]

