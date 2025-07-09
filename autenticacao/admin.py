from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario
from .forms import CadastroForm, AtualizacaoUsuarioForm

class UsuarioAdmin(UserAdmin):
    add_form = CadastroForm
    form = AtualizacaoUsuarioForm
    model = Usuario
    list_display = ['email', 'nome', 'cidade', 'is_staff', 'is_active',]
    
    # Esta seção define os campos para EDITAR um usuário.
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Informações Pessoais', {'fields': ('nome', 'foto_perfil', 'cidade', 'latitude', 'longitude')}),
        ('Permissões', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Datas Importantes', {'fields': ('last_login',)}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password', 'password2'),
        }),
    )
    
    search_fields = ('email', 'nome',)
    ordering = ('email',)

admin.site.register(Usuario, UsuarioAdmin)