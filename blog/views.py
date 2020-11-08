from django.shortcuts import render
from blog.models import Post,Categoria


# Create your views here.

def blog(request):
    posts=Post.objects.all()
    Cate=Categoria.objects.all()

    return render(request,'blog/blog.html',{'posts':posts, 'Cate':Cate})



def blogcategoria(request,Id_categoria):
    posts=Post.objects.all()
    Cate=Categoria.objects.get(id=Id_categoria)
    posts=Post.objects.filter(categorias=Cate)

    return render(request,'blog/pstcategoria.html',{'posts':posts, 'Cate':Cate})


