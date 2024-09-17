from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('callback/', views.callback, name='callback'),  # La URL a la que Auth0 redirige después del login
    path('dashboard/', views.dashboard, name='dashboard'),  # El dashboard después del login
    path('logout/', views.logout, name='logout'),
]
