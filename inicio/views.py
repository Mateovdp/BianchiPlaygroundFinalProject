from django.shortcuts import render, redirect
from django.http import HttpResponse
from inicio.models import Empleado, DatosExtras
from inicio.forms import FormularioCreacionEmpleado, FormularioEdicionEmpleado, BusquedaEmpleado, CreaciondeUsuario, EditarPerfil
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm
from django.contrib.auth import authenticate, login as django_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy




##################  NAV-BAR  ####################

def inicio(request):
    
    empleados = Empleado.objects.all()
    return render(request, 'inicio/inicio.html', {'empleados':empleados})

@login_required
def inicior(request):
    
    empleados = Empleado.objects.all()
    return render(request, 'inicio/inicior.html', {'empleados':empleados})


def nosotros(request):
     return render(request, 'inicio/nosotros.html')


def contacto(request):
    return render(request, 'inicio/contacto.html')


##################  CONTROL DE EMPLEADOS  ###################

@login_required
def lista(request):
    empleados = Empleado.objects.all()

    if request.method == 'GET' and 'nombre' in request.GET:
        formulario = BusquedaEmpleado(request.GET)
        if formulario.is_valid():
            nombre_a_buscar = formulario.cleaned_data.get('nombre')
            empleados = Empleado.objects.filter(nombre__icontains=nombre_a_buscar)
            
    else:
        formulario = BusquedaEmpleado()

    return render(request, 'inicio/lista.html', {'empleados': empleados, 'formulario': formulario})

@login_required
def crear_empleado(request):
    formulario = FormularioCreacionEmpleado()
    if request.method == 'POST':
        formulario = FormularioCreacionEmpleado(request.POST)
        if formulario.is_valid():
            nombre = formulario.cleaned_data.get('nombre')
            apellido = formulario.cleaned_data.get('apellido')
            documento = formulario.cleaned_data.get('documento')
            localidad = formulario.cleaned_data.get('localidad')  
            informacion = formulario.cleaned_data.get('informacion')      
            empleado = Empleado(nombre=nombre, apellido=apellido, documento=documento, localidad=localidad, informacion=informacion)
            empleado.save()
            return redirect('lista')

    empleados = Empleado.objects.all()

    return render(request, 'inicio/crear_empleado.html',{'formulario' : formulario, 'empleados': empleados})


@login_required
def ver_empleado(request, id_empleado):
    empleado = Empleado.objects.get(id=id_empleado)
    return render(request, 'inicio/ver_empleado.html',{'empleado':empleado})


@login_required
def eliminar_empleado(request, id_empleado):
    empleado = Empleado.objects.get(id=id_empleado)
    empleado.delete()
    return redirect('lista')


@login_required
def editar_empleado(request, id_empleado):
    empleado = Empleado.objects.get(id=id_empleado)
    formulario = FormularioEdicionEmpleado(initial={'nombre': empleado.nombre, 'apellido': empleado.apellido, 'documento' : empleado.documento, 'localidad': empleado.localidad, 'informacion': empleado.informacion })

    if request.method == 'POST':
        formulario = FormularioEdicionEmpleado(request.POST)
        if formulario.is_valid():
            info_nueva = formulario.cleaned_data

            empleado.nombre = info_nueva.get('nombre')
            empleado.apellido = info_nueva.get('apellido')
            empleado.documento = info_nueva.get('documento')
            empleado.localidad = info_nueva.get('localidad')
            empleado.informacion = info_nueva.get('informacion')

            empleado.save()
            return redirect('lista')

    return render(request, 'inicio/editar_empleado.html', {'empleado':empleado, 'formulario':formulario})


################  USUARIOS  ################ 

def login(request):
    formulario = AuthenticationForm()
    if request.method == "POST":
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            usuario = formulario.cleaned_data.get('username')
            contraseña = formulario.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contraseña)

            django_login(request, user)

            return redirect('inicior')

    return render(request, 'inicio/login.html', {'formulario':formulario})




def registro(request):
    formulario = CreaciondeUsuario()

    if request.method == 'POST':
        formulario = CreaciondeUsuario(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('login')
    return render(request, 'inicio/registro.html', {'formulario': formulario})

@login_required
def perfil(request):
    return render(request,'inicio/perfil.html')

@login_required
def editar_perfil(request):
    
    user = request.user
    datos_extra, _= DatosExtras.objects.get_or_create(user=user)

    if request.method == 'POST':
        formulario = EditarPerfil(request.POST, request.FILES, instance=request.user)
        if formulario.is_valid():
            avatar = formulario.cleaned_data.get('avatar')
            if avatar:
                datos_extra.avatar = avatar

            datos_extra.save()
            formulario.save()
            return redirect('perfil')
    else:
        formulario = EditarPerfil(initial={'avatar': datos_extra.avatar}, instance=request.user)
    return render(request,'inicio/editar_perfil.html', {'formulario':formulario})
    

class EditarContrasenia(PasswordChangeView):
    template_name = 'inicio/cambiar_contrasenia.html'
    success_url = reverse_lazy('perfil')
    