from django.db import models
from autenticacao.models import Usuario 

class RegistroCrescimento(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    data_registro = models.DateTimeField(auto_now_add=True)
    altura_cm = models.DecimalField(max_digits=5, decimal_places=2, help_text="Altura da planta em centímetros")
    numero_folhas = models.PositiveIntegerField(default=0, help_text="Número de folhas da planta")
    foto_planta = models.ImageField(upload_to='fotos_plantas/', blank=True, null=True, help_text="Uma foto da planta no dia do registro")
    anotacoes = models.TextField(blank=True, null=True, help_text="Observações gerais sobre a planta")

    class Meta:
        ordering = ['-data_registro'] # Ordena os registros do mais novo para o mais antigo

    def __str__(self):
        return f"Registro de {self.usuario.nome} em {self.data_registro.strftime('%d/%m/%Y')}"
    
class UmidadeDiaria(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    data = models.DateField() 
    umidade_media = models.FloatField(help_text="Umidade média registrada no dia (%)")

    class Meta:
        ordering = ['-data']
        verbose_name = "Umidade Diária"
        verbose_name_plural = "Umidades Diárias"
        unique_together = ('usuario', 'data') 

    def __str__(self):
        return f"{self.data.strftime('%d/%m/%Y')} - {self.umidade_media}%"