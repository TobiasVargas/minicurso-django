from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Contrato, Aditivo
from .serializers import ContratoSerializer, AditivoSerializer


class ContratoViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Contrato.objects.all()
    serializer_class = ContratoSerializer


class AditivoViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Aditivo.objects.all()
    serializer_class = AditivoSerializer
