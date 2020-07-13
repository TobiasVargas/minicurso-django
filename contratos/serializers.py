from rest_framework import serializers
from .models import Contrato
from django.contrib.auth.models import User


class ContratoSerializer(serializers.HyperlinkedModelSerializer):
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
                  'arquivo']
