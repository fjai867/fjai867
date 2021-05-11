from django.shortcuts import render,redirect
#from django.http import HttpResponse
#from gestion_atletas.forms import fmrAtletas,fmrAtletasEdit
#from django.contrib.auth import authenticate
#from django.contrib.auth import logout as do_logout
#from django.contrib.auth import login as do_login
#from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,User
from gestion_atletas.models import Prueba
from django.views.generic import  ListView
#from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.conf import settings






# Create your views here.




def administrador(request):
    return redirect("admin")


def inicio(request):

    return render(request,"gestion_atletas/inicio.html")
    

def calendario(request):

   return render(request,"gestion_atletas/calendario.html")


def contacto(request):

    if request.method=="POST":

        subject=request.POST["asunto"]
        message=request.POST["mensaje"] +" "+request.POST["email"]
        email_from=settings.EMAIL_HOST_USER
        recipient_list=["fjai***@gmail.com"]
        send_mail(subject,message,email_from,recipient_list)
        return render(request,"gestion_atletas/contactogracias.html")


    return render(request,"gestion_atletas/contacto.html")


class ListaPr(ListView):
    model=Prueba
    template_name='gestion_atletas/listado1.html'
   



