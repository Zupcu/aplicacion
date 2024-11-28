from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import LoginForm, RegistroForm, ClienteForm
from .models import Cliente, Usuario

# Vista de inicio
def inicio(request):
    return render(request, 'inicio.html')

# Vista de login
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

# Vista de registro
def registro_view(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = Usuario.USER  # Asignar el rol predeterminado
            user.save()
            messages.success(request, 'Usuario creado con éxito')
            return redirect('login')
    else:
        form = RegistroForm()
    return render(request, 'registro.html', {'form': form})

# Vista del dashboard (panel de control)
@login_required
def dashboard(request):
    clientes = Cliente.objects.all()
    return render(request, 'dashboard.html', {'clientes': clientes})

# Vista para agregar o editar clientes
@login_required
def cliente_form(request, id=None):
    if id:
        cliente = Cliente.objects.get(id=id)
    else:
        cliente = Cliente()
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'cliente_form.html', {'form': form})

# Vista para eliminar cliente
@login_required
def cliente_eliminar(request, id):
    cliente = Cliente.objects.get(id=id)
    cliente.delete()
    return redirect('dashboard')

