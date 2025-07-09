import requests
import random

from datetime import timedelta
from django.utils import timezone
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash

from autenticacao.forms import AtualizacaoUsuarioForm, CustomPasswordChangeForm
from .models import RegistroCrescimento, UmidadeDiaria
from .forms import RegistroCrescimentoForm


# View da API interna para buscar cidades
@login_required
def search_city(request):
    city_query = request.GET.get('q')
    state_query = request.GET.get('state')

    if not city_query:
        return JsonResponse({'error': 'Nenhuma cidade informada.'}, status=400)

    try:
        geo_url = 'https://geocoding-api.open-meteo.com/v1/search'
        params = {'name': city_query, 'count': 50, 'language': 'pt', 'format': 'json'}
        geo_response = requests.get(geo_url, params=params)
        geo_response.raise_for_status()
        data = geo_response.json()

        if 'results' in data and state_query:
            filtered_results = [city for city in data['results'] if 'admin1' in city and state_query.lower() in city['admin1'].lower()]
            data['results'] = filtered_results

        return JsonResponse(data)
    except requests.exceptions.RequestException:
        return JsonResponse({'error': 'Erro ao conectar ao serviço de geolocalização.'}, status=500)


# View da API interna para buscar previsão do tempo
@login_required 
def get_weather_data(request):
    user = request.user
    if user.latitude and user.longitude:
        try:
            params = {
                "latitude": user.latitude,
                "longitude": user.longitude,
                "daily": "weathercode,temperature_2m_max,temperature_2m_min,precipitation_probability_max",
                "forecast_days": 7,
                "timezone": "America/Sao_Paulo"
            }
            weather_response = requests.get("https://api.open-meteo.com/v1/forecast", params=params)
            weather_response.raise_for_status()
            return JsonResponse(weather_response.json())
        except requests.exceptions.RequestException:
            return JsonResponse({"error": "Não foi possível conectar ao serviço de clima."}, status=500)
    return JsonResponse({"error": "Localização não definida no perfil."}, status=400)


# View do Dashboard Principal
@login_required 
def dashboard_view(request):
    # Lógica para processar os formulários do modal de configurações
    if request.method == 'POST':
        if 'update_profile' in request.POST:
            user_form = AtualizacaoUsuarioForm(request.POST, request.FILES, instance=request.user)
            if user_form.is_valid():
                user_form.save()
                messages.success(request, 'Seus dados foram atualizados com sucesso!')
                return redirect('dashboard')
        elif 'change_password' in request.POST:
            password_form = CustomPasswordChangeForm(user=request.user, data=request.POST)
            if password_form.is_valid():
                user = password_form.save()
                update_session_auth_hash(request, user)
                messages.success(request, 'Sua senha foi alterada com sucesso!')
                return redirect('dashboard')
    
    # Prepara os formulários para serem passados para o template
    user_form = AtualizacaoUsuarioForm(instance=request.user)
    password_form = CustomPasswordChangeForm(user=request.user)

    context = {
        'page_name': 'dashboard', # Informa ao base.html qual página está ativa
        'user_form': user_form,
        'password_form': password_form,
    }
    return render(request, 'dashboard.html', context)


# View da Página de Histórico
@login_required
def historico_view(request):
    # Processa o formulário de NOVO REGISTRO
    if request.method == 'POST':
        form = RegistroCrescimentoForm(request.POST, request.FILES)
        if form.is_valid():
            novo_registro = form.save(commit=False)
            novo_registro.usuario = request.user
            novo_registro.save()
            messages.success(request, 'Novo registro de crescimento salvo!')
            return redirect('historico')
    else:
        form = RegistroCrescimentoForm()

    # Busca todos os registros do usuário logado
    registros = RegistroCrescimento.objects.filter(usuario=request.user)
    
    # Prepara os formulários do MODAL para serem passados para o template
    user_form = AtualizacaoUsuarioForm(instance=request.user)
    password_form = CustomPasswordChangeForm(user=request.user)

    context = {
        'page_name': 'historico', # caso seja criado um 'base.html'
        'registros': registros,
        'form': form,
        'user_form': user_form,         
        'password_form': password_form, 
    }
    return render(request, 'historico.html', context)

# View do Gráfico de Umidade
@login_required
def dados_umidade_dashboard(request):
    usuario = request.user
    hoje = timezone.now().date()
    dados = []

    # Loop pelos últimos 7 dias, do mais antigo para o mais novo
    for i in range(6, -1, -1):
        dia_atual = hoje - timedelta(days=i)
        
        # Tenta encontrar um registro para este dia
        registro, criado = UmidadeDiaria.objects.get_or_create(
            usuario=usuario,
            data=dia_atual,
            # 'defaults' só é usado se o objeto for criado
            defaults={'umidade_media': round(random.uniform(55.0, 75.0), 2)}
        )
        
        # Adiciona os dados formatados à nossa lista
        dados.append({
            'data': registro.data.strftime('%d/%m'),
            'valor': registro.umidade_media
        })

    # Extrai os labels e valores para o gráfico
    labels = [d['data'] for d in dados]
    valores = [d['valor'] for d in dados]

    return JsonResponse({'labels': labels, 'valores': valores})

@login_required
def change_password_api(request):
    if request.method == 'POST':
        form = CustomPasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Mantém o usuário logado
            return JsonResponse({'status': 'success', 'message': 'Senha alterada com sucesso!'})
        else:
            # Se o formulário for inválido, retorna os erros em formato JSON
            return JsonResponse({'status': 'error', 'errors': form.errors.as_json()}, status=400)
    
    # Retorna um erro se não for um método POST
    return JsonResponse({'error': 'Método não permitido'}, status=405)

# View temporária para testar a página 500
def teste_erro_500(request):
    divisao_por_zero = 1 / 0
    return render(request, 'dashboard.html')