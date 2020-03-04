from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .models import Luminosity
from .serializers import LuminositySerializer

class LuminosityViewSet(viewsets.ModelViewSet):
    queryset = Luminosity.objects.all().order_by('-created')
    serializer_class = LuminositySerializer