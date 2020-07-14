from django.shortcuts import render
from rest_framework import viewsets
from .models import Contrato, Aditivo
from .serializers import ContratoSerializer, AditivoSerializer


# Create your views here.
class ContratoViewSet(viewsets.ModelViewSet):
    queryset = Contrato.objects.all()
    serializer_class = ContratoSerializer

class AditivoViewSet(viewsets.ModelViewSet):
    queryset = Aditivo.objects.all()
    serializer_class = AditivoSerializer
