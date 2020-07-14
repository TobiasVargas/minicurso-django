from rest_framework import serializers
from .models import Contrato, Aditivo
from django.contrib.auth.models import User


class AditivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aditivo
        fields = ['id',
                  'descricao',
                  'arquivo']



class ContratoSerializer(serializers.ModelSerializer):
    aditivos = AditivoSerializer(many=True) #read_only=True
    class Meta:
        model = Contrato
        fields = ['id',
                  'numero_contrato',
                  'valor',
                  'descricao',
                  'data_inicio',
                  'data_fim',
                  'tipo',
                  'status',
                  'motivo_cancelamento',
                  'criado_em',
                  'atualizado_em',
                  'arquivo',
                  'aditivos']


