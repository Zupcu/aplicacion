from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('login/', views.login_view, name='login'),
    path('registro/', views.registro_view, name='registro'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('cliente/', views.cliente_form, name='cliente_form'),  # URL para crear un nuevo cliente
    path('cliente/<int:id>/', views.cliente_form, name='cliente_form_edit'),  # URL para editar un cliente existente
    path('cliente/eliminar/<int:id>/', views.cliente_eliminar, name='cliente_eliminar'),
]

