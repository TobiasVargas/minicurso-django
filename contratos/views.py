from django.shortcuts import render
from rest_framework import viewsets
from .models import Contrato
from .serializers import ContratoSerializer


# Create your views here.
class ContratoViewSet(viewsets.ModelViewSet):
    queryset = Contrato.objects.all()
    serializer_class = ContratoSerializer
