from django import forms
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, UserChangeForm
from .models import Usuario

class CadastroForm(forms.ModelForm):
    password = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(attrs={'placeholder': 'Insira uma senha', 'id': 'id_password'})
    )
    password2 = forms.CharField(
        label='Confirmar Senha',
        widget=forms.PasswordInput(attrs={'placeholder': 'Repetir senha', 'id': 'id_password2'})
    )

    class Meta:
        model = Usuario
        fields = ('email',)
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'Seu melhor e-mail'}),
        }

    def clean_password2(self):
        cd = self.cleaned_data
        if cd.get('password') and cd.get('password2') and cd['password'] != cd['password2']:
            raise forms.ValidationError("ERRO: AS SENHAS NÃO COINCIDEM.")
        return cd.get('password2')

    # CRIPTOGRAFAR A SENHA #
    def save(self, commit=True):
        # Pega a instância do usuário do formulário, mas não salva ainda
        user = super().save(commit=False)
        # Define a senha usando o método que faz a criptografia (hashing)
        user.set_password(self.cleaned_data["password"])
        
        # Se estiver sendo criado pelo Admin, marca como staff para permitir acesso
        if self.is_staff_user_creation():
            user.is_staff = True
            
        if commit:
            user.save()
        return user

    # Função auxiliar para detectar se o form está no admin
    def is_staff_user_creation(self):
        # Uma forma de checar se o formulário está sendo usado para criar um usuário staff
        return self.data.get('is_staff') == 'on'

class LoginForm(AuthenticationForm):
    username = forms.EmailField(
        label="E-mail",
        widget=forms.EmailInput(attrs={'autofocus': True, 'placeholder': 'E-mail'})
    )
    password = forms.CharField(
        label="Senha",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'placeholder': 'Senha'}),
    )
    error_messages = {
        'invalid_login': "ERRO: e-mail ou senha inválidos.",
        'inactive': "Esta conta está inativa.",
    }

class AtualizacaoUsuarioForm(forms.ModelForm): 
    class Meta:
        model = Usuario
        
        fields = ('nome', 'email', 'foto_perfil', 'cidade', 'latitude', 'longitude')
        # Adicionamos widgets para os campos que não devem ser visíveis
        widgets = {
            'latitude': forms.HiddenInput(),
            'longitude': forms.HiddenInput(),
            'cidade': forms.TextInput(attrs={'placeholder': 'Digite o nome de uma cidade'})
        }
        
class CustomPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super(CustomPasswordChangeForm, self).__init__(*args, **kwargs)
        self.fields['old_password'].widget = forms.PasswordInput(attrs={'placeholder': 'Senha atual'})
        self.fields['new_password1'].widget = forms.PasswordInput(attrs={'placeholder': 'Nova senha'})
        self.fields['new_password2'].widget = forms.PasswordInput(attrs={'placeholder': 'Confirmar nova senha'})