from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Contrato (models.Model):
    TIPOS_CONTRATO_CHOICES = [
        ('1', 'Nome1'),
        ('2', 'Nome2'),
        ('3', 'Nome3'),
    ]

    STATUS_CHOICES = [
        ('1', 'Ativo'),
        ('2', 'Cancelado'),
    ]

    numeroContrato = models.CharField(max_length=50)
    valor = models.DecimalField(max_digits=15, decimal_places=2)
    descricao = models.TextField(blank=True, null=True)
    data_inicio = models.DateField()
    data_fim = models.DateField()
    tipo = models.CharField(max_length=1, choices=TIPOS_CONTRATO_CHOICES)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='1')
    motivo_cancelamento = models.TextField(null=True, blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    arquivo = models.FileField(upload_to='files_contratos/')
    usuario = User