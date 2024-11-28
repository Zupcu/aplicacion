from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Cliente, Usuario

# Formulario de login
class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=255, label='Usuario')
    password = forms.CharField(widget=forms.PasswordInput, label='Contraseña')

# Formulario de registro de usuario
class RegistroForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['username', 'password1', 'password2']

# Formulario de cliente
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido', 'email', 'telefono', 'direccion']
