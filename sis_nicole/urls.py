from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    path('clientes/', include('clientes.urls')),  # <- aquí agregas esta línea
]
