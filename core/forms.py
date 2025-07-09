from django import forms
from .models import RegistroCrescimento

class RegistroCrescimentoForm(forms.ModelForm):
    class Meta:
        model = RegistroCrescimento
        
        fields = ['altura_cm', 'numero_folhas', 'foto_planta', 'anotacoes']