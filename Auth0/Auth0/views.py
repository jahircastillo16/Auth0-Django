# Auth0/views.py

from django.shortcuts import redirect
from django.http import HttpResponse

def login(request):
    return render(request, 'login.html')

def callback(request):
    # Aquí deberías manejar el código de autorización o el JWT recibido de Auth0
    # Este es un ejemplo simple que redirige a una página de bienvenida

    # Para un manejo real, necesitarías obtener el token de la consulta y
    # validarlo con Auth0, pero para fines demostrativos, redirigimos al dashboard.
    return redirect('dashboard')  # Redirige a la vista de dashboard
