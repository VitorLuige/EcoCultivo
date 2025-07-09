from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_view, name='dashboard'),
    path('dashboard/', views.dashboard_view, name='dashboard_escrito'),
    path('historico/', views.historico_view, name='historico'),
    path('api/weather/', views.get_weather_data, name='get_weather_data'),
    path('api/search-city/', views.search_city, name='search_city'),
    path('dashboard/dados-umidade/', views.dados_umidade_dashboard, name='dados_umidade_dashboard'),
    path('api/change-password/', views.change_password_api, name='change_password_api'),
    path('erro/', views.teste_erro_500, name='teste_erro'),
]
