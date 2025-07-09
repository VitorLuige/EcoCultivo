from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import CadastroForm, LoginForm

def cadastro_view(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False) # Cria o objeto de usuário, mas não salva no banco ainda
            user.set_password(form.cleaned_data['password']) # Criptografa e define a senha
            user.save() # Agora salva o usuário no banco de dados com a senha segura

            messages.success(request, 'Cadastro realizado com sucesso! Por favor, faça o login.')
            return redirect('autenticacao:login')
    else:
        form = CadastroForm()
    
    return render(request, 'cadastro.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                if request.POST.get('remember'):
                    request.session.set_expiry(1209600) 
                else:
                    request.session.set_expiry(0)
                return redirect('dashboard')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.info(request, 'Você saiu da sua conta.')
    return redirect('autenticacao:login')