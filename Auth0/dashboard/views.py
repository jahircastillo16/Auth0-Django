from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django_auth0.backend import get_user_profile

def login(request):
    """ Redirige a la página de login de Auth0 """
    return redirect('https://<YOUR_AUTH0_DOMAIN>/authorize?client_id=<YOUR_CLIENT_ID>&response_type=code&scope=openid profile email&redirect_uri=http://localhost:8000/callback')

def callback(request):
    """ Maneja la respuesta de Auth0 después del login """
    profile = get_user_profile(request)
    if profile:
        # Guarda la información del perfil en la sesión
        request.session['user_profile'] = profile
        return redirect('dashboard')
    return redirect('login')

@login_required
def dashboard(request):
    """ Muestra el dashboard solo si el usuario está autenticado """
    user_profile = request.session.get('user_profile', {})
    return render(request, 'dashboard.html', {'user_profile': user_profile})

def logout(request):
    """ Cierra la sesión y redirige al usuario al login """
    request.session.flush()  # Elimina los datos de la sesión
    return redirect('https://<YOUR_AUTH0_DOMAIN>/v2/logout?client_id=<YOUR_CLIENT_ID>&returnTo=http://localhost:8000/')
