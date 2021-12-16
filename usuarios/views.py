
from django.shortcuts import render,redirect
from django.http import HttpResponse
from gestion_atletas.forms import fmrAtletas,fmrAtletasEdit,Nuevo_PasswordChangeForm
from django.contrib.auth import authenticate
from django.contrib.auth import logout as do_logout
from django.contrib.auth import login as do_login
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,User
from gestion_atletas.models import Atleta,Prueba,Categoria,Inscripcion
from django.views.generic import UpdateView, ListView,CreateView,DeleteView, View
from django.urls import reverse_lazy
import datetime
from usuarios.utiles import genera_pdf
from django.contrib.auth.views import PasswordChangeView,PasswordChangeDoneView



# Create your views here.
#vista para actualizar usuarios
def registro(request, Id_Atl):
    #instanciamos los datos correspondientes al Atleta_Id
    
    ins=Atleta.objects.get(pk=Id_Atl)
    

    #creamos el formulario con la instancia obtenida
    form=fmrAtletas(instance=ins)
    

    #recuperamos los datos modificados

    if request.method =='POST':
        
        form=fmrAtletas(data=request.POST)
        
        #si es valido
        if form.is_valid():

            form.save(commit=False)
            form.save()
          
            
            
        return render(request,'usuarios/inicioclientes.html')
        
        
    return render(request,'usuarios/registro.html',{'form':form})

#vista para el registro de datos de Atleta
def registroB(request):
    
    if request.method=='POST':
        form=fmrAtletas(data=request.POST)
        

        if form.is_valid():
            #instanciar Ultimo registro de usuario
            Us=User.objects.last()
           
    
           
            
            #instanciamos atleta y añadimos la relacion uno a uno Usuario/atleta
            instancia=Atleta(
                Num_Matri=form.cleaned_data['Num_Matri'],
                Nom=form.cleaned_data['Nom'],
                Ape=form.cleaned_data['Ape'],
                Dire=form.cleaned_data['Dire'],
                Pobla=form.cleaned_data['Pobla'],
                Cod_Pos=form.cleaned_data['Cod_Pos'],
                Tel=form.cleaned_data['Tel'],
                Fecha_Nac=form.cleaned_data['Fecha_Nac'],
                email=form.cleaned_data['email'],
                username=Us,
            )
            
            
            #Grabar Nuevo registro atleta
            instancia.save()

            #grabar mail en modelo Usuario
            Us.email=form.cleaned_data['email']
            Us.first_name=form.cleaned_data['Nom']
            Us.last_name=form.cleaned_data['Ape']
            Us.save()
            
            
            return render(request,'usuarios/regcorrecto.html')
    else:
        form=fmrAtletas()
        
        
    return render(request,'usuarios/registrob.html',{'form':form})    

def Codigo1(request):
    if request.method=='POST':
        codigoA=request.POST['codigoacces']
        if codigoA=='ABCD':
            return redirect('/register/') 
             


    return render(request,'usuarios/codigo_acceso.html')
    
    



def login(request):
    # Creamos el formulario de autenticación vacío
    form = AuthenticationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = AuthenticationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Recuperamos las credenciales validadas
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Verificamos las credenciales del usuario
            Atuser = authenticate(username=username, password=password)
            
            # Si existe un usuario con ese nombre y contraseña
            if Atuser is not None:
               
                # Hacemos el login manualmente
                do_login(request, Atuser)
                # Y le redireccionamos a la portada
                
                contexto={'clientes':Atuser}
                return render(request,'usuarios/areaclientes.html',contexto)

    # Si llegamos al final renderizamos el formulario
    return render(request, "usuarios/login2.html")   

def register(request):
    # Creamos el formulario de autenticación vacío
    form = UserCreationForm()
    # modificamos los campos de ayuda del formulario
    form.fields['username'].help_text = """<p style="color:#efeef0"> Requerido 150 cararteres como máximo.Unicamente letras y dígitos </p>"""
    form.fields['password1'].help_text = """<p style="color:#efeef0">* Su contraseña debe tener al menos 8 caracteres</p>
    <p style="color:#efeef0">* Su contraseña no puede ser completamente numérica</p>"""
    form.fields['password2'].help_text = """<p style="color:#efeef0"> Confirme de nuevo su contraseña </p>"""
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = UserCreationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():

            # Creamos la nueva cuenta de usuario
            Atuser = form.save()

            # Si el usuario se crea correctamente 
            if Atuser is not None:
                 #guradamos el nombre de usuario para pasarlo por argumento
                
                # Hacemos el login manualmente
                do_login(request, Atuser)
                # Y le redireccionamos a la portada
                #return redirect('/regcorrecto')
                
                return redirect("/registro_datos/")


    # Si llegamos al final renderizamos el formulario
    return render(request, "usuarios/register.html", {'form': form})

def logout(request):
    #finalizamos la sesion
    do_logout(request)
    #retornamos a inicio
    return redirect('/inicio')

def registrocorrecto(request):
    return render(request,"usuarios/regcorrecto.html")

def inscricorrecto(request):
    return render(request,"usuarios/inscorrecta.html")


def inicioclientes(request):
    return render(request,"usuarios/inicioclientes.html")

def usuario(request):
    return render(request,'usuarios/usuario.html')

#funcion ListarCat ??????????????????????????????????????????
def ListarCat(request,IdPr):
    MiLista=Categoria.objects.filter(Id_Prueba=IdPr)
    contexto={'categoria':MiLista}
    return render(request,'usuarios/categorias.html',contexto)

def GrabarIns(request,Id_Cat):

   
    #usuario logueado
    usuario1=request.user
    
    #item de categoria
    Cat1=Categoria.objects.get(pk=Id_Cat)
    usuario=Inscripcion.objects.create(username=usuario1,Id_Cat=Cat1, Id_Prueba=Cat1.Id_Prueba)
    usuario.save()
    
    return render(request,'usuarios/inscorrecta.html')



class Atleta_edit(UpdateView):
    model=Atleta
    form_class=fmrAtletasEdit
    template_name='usuarios/edicionat.html'
    slug_field = 'username'
    success_url=reverse_lazy('area_clientes')

#lista de pruebas sin filtros ??????????????????????????????????????
#class ListaPrCli(ListView):
    #model=Prueba
    #template_name='usuarios/listado2.html'

#lista con filtros fecha de inicio y fecha de fin
class ListaPrCliFecha(ListView):
    model=Prueba
    template_name='usuarios/listado2.html'
    def get_queryset(self):
        fecha_actual=datetime.datetime.now()
        return Prueba.objects.filter(Fecha_Fin__gte= fecha_actual, Fecha_Inicio__lte=fecha_actual)


class ListaCatCli(ListView):
    model=Categoria
    template_name='usuarios/listado3.html'
    slug_field = 'Id_Prueba'
    def get_queryset(self):
        id_Prueba = self.kwargs['Id_Prueba']
        return Categoria.objects.filter(Id_Prueba=id_Prueba)


class ListadoIns(ListView):
    model=Inscripcion
    template_name='usuarios/listado4.html'
    def get_queryset(self):
        usuario1=self.request.user
        return Inscripcion.objects.filter(username=usuario1).select_related("Id_Cat")

class BorrarIns(DeleteView):
    model=Inscripcion
    template_name='usuarios/borrarIns.html'
    success_url=reverse_lazy('listado4')
    
class LisPruebas(ListView):
    model=Prueba
    template_name='usuarios/listado5.html'
    def get_queryset(self):
        fecha_actual=datetime.datetime.now()
        return Prueba.objects.filter(Fecha_Fin__gte= fecha_actual, Fecha_Inicio__lte=fecha_actual)

class LisInscritos(ListView):
    model=Inscripcion
    template_name='usuarios/listado6.html'
    slug_field='Id_Prueba'
    #context_object_name='inscripcion'

    def get_queryset(self):
        id_Prueba = self.kwargs['Id_Prueba']
        return Inscripcion.objects.filter(Id_Prueba=id_Prueba).select_related('username')

    
class lista_pdf(View):
    slug_field='Id_Ins'
    #slug_field='Id_Prueba'
    
    
    def get(self, request,*args, **kwargs):
        #id_Prueba = self.kwargs['Id_Prueba']
        id_Ins=self.kwargs['Id_Ins']
        obj1=Inscripcion.objects.get(Id_Ins=id_Ins)
        prueba=obj1.Id_Prueba

        #inscripcion=Inscripcion.objects.all().select_related('username')
        inscripcion=Inscripcion.objects.filter(Id_Prueba=prueba).select_related('username')
        data={
            'inscripcion':inscripcion
        } 
        pdf=genera_pdf('usuarios/listado6pdf.html',data)
        return HttpResponse(pdf, content_type='application/pdf')

#cambiar la contraseña
class Cambiar_password(PasswordChangeView):
    template_name='usuarios/contraseña_nueva.html'
    form_class= Nuevo_PasswordChangeForm

#politica de privacidad
def politica(request):
    return render(request,"usuarios/politica.html")

#politica de coockies
def cokies(request):
    return render(request,"usuarios/cokis.html")







   
   


    
   
    
    
        








