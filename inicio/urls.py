from django.urls import path
from inicio.views import inicio, CrearEmpleado, lista, nosotros, contacto, ver_empleado, eliminar_empleado, editar_empleado, login, registro, perfil, editar_perfil, EditarContrasenia
from django.contrib.auth.views import LogoutView


urlpatterns = [
    #nav-bar
    path('', inicio, name='inicio'),
    path('nosotros/', nosotros, name= 'nosotros'),
    path('contactanos/', contacto, name= 'contacto'),
    #control de empleados
    path('registrados/', lista, name= 'lista'),
    path('crear_empleado/', CrearEmpleado.as_view(), name= 'crear_empleado'),
    path('empleado/<int:id_empleado>/', ver_empleado, name= 'ver_empleado'),
    path('empleado/<int:id_empleado>/eliminar/', eliminar_empleado, name= 'eliminar_empleado'),
    path('empleado/<int:id_empleado>/editar/', editar_empleado, name= 'editar_empleado'),
    #usuarios
    path('login/', login, name= 'login'),
    path('logout/', LogoutView.as_view(template_name='inicio/logout.html'), name = 'logout'),
    path('registro/', registro, name= 'registro'),
    path('perfil/', perfil, name= 'perfil'),
    path('perfil/editar/', editar_perfil, name= 'editar_perfil'),
    path('perfil/cambiar_contraseña/', EditarContrasenia.as_view(), name= 'cambiar_contrasenia'),


]