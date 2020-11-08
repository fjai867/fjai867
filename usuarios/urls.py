

from django.urls import path
from usuarios import views
from django.contrib.auth.views import PasswordChangeDoneView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    
    #iniciar sesion
    path("accounts/login/",views.login,name='login'),
    #inciar sesion  mas datos
    path("registro/<int:Id_Atl>",views.registro,name='registro'),
    #desconectar sesion
    path("/",views.logout,name="logout"),
    #Registrar usuario y contraseña
    path("register/",views.register,name="register"),
    #registrar usuario y password
    path("usuario/",views.usuario,name="usuario"),
    #plantilla area clientes 
    path("area_clientes/",login_required(views.inicioclientes),name="area_clientes"),
    path("regcorrecto/",views.registrocorrecto,name="regcorrecto"),
    #grabar datos del usuario-mail-direccion-poblacion-ect.
    path("registro_datos/",views.registroB,name='registro_datos'),
    #edicion de datos de usuario
    path("editar/<slug>",login_required(views.Atleta_edit.as_view()),name='editar'),
    #listado de pruebas pendientes????????????????????
    #path("listado2/",views.ListaPrCli.as_view(),name="listado2"),
    #listado categorias de la prueba indicada en el parametro ????????????????
    path("liscat/<int:Id_Prueba>",views.ListarCat,name="liscat"),
    #listado categorias de la prueba indicada en el parametro
    path("liscategoria/<int:Id_Prueba>/",login_required(views.ListaCatCli.as_view()),name="liscategoria"), 
    path("insCorrecto/",views.inscricorrecto,name="insCorrecto"),
    #grabar inscripcion
    path("inscripcion2/<int:Id_Cat>",login_required(views.GrabarIns),name="inscripcion2"),
    #listado de pruebas inscritas por atleta
    path("listado4/",login_required(views.ListadoIns.as_view()),name="listado4"),
    #borrar inscripcion
    path("borrar/<int:pk>",login_required(views.BorrarIns.as_view()),name="borrar"),
    #listado de pruebas pendientes por fechas
    path("listado22/",login_required(views.ListaPrCliFecha.as_view()),name="listado22"),
    #informacion de listado de pruebas con sus inscripciones
    path("lispruebas/",login_required(views.LisPruebas.as_view()),name="lispruebas"), 
    #lista inscritos
    path("listaInscritos/<int:Id_Prueba>/",login_required(views.LisInscritos.as_view()),name="listaInscritos"),
    #Lista pdf inscritos
    path("listaInscritospdf/<int:Id_Ins>/",login_required(views.lista_pdf.as_view()),name="listaInscritospdf"),
    #cambiar contraseña
    path("change_password/",views.Cambiar_password.as_view(),name="change_password"), 
    path("password_change_done",PasswordChangeDoneView.as_view(template_name='usuarios/password_change_done.html'),name='password_change_done'),
    #acceso con codigo
    path('Codigo/',views.Codigo1, name='Codigo'),
    
    
    

]
