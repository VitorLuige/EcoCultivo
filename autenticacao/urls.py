from django.urls import path
from . import views

app_name = 'autenticacao'

urlpatterns = [
    path('cadastro/', views.cadastro_view, name='cadastro'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]