from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

class FormularioBaseEmpleado(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    documento = forms.IntegerField()
    localidad = forms.CharField(max_length=20)
    informacion = forms.CharField(max_length=500)


class FormularioCreacionEmpleado(FormularioBaseEmpleado):
    ...

class FormularioEdicionEmpleado(FormularioBaseEmpleado):
    ...

class BusquedaEmpleado(forms.Form):
   nombre = forms.CharField(max_length=20, required=False)


class CreaciondeUsuario(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir Contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {llave:'' for llave in fields}


class EditarPerfil(UserChangeForm):
    password = None
    forms.EmailField(label='Editar el email')
    first_name = forms.CharField(label='Nombre')
    last_name = forms.CharField(label='Apellido')
    avatar = forms.ImageField(required=False)
    
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']