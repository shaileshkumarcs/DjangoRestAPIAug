from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Languages, Paradigms, Programmers
from .serializers import LanguageSerializer, ParadigmSerializer, ProgrammerSerializer

class LanguageView(viewsets.ModelViewSet):
    queryset = Languages.objects.all()
    serializer_class = LanguageSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class ParadigmView(viewsets.ModelViewSet):
    queryset = Paradigms.objects.all()
    serializer_class = ParadigmSerializer

class ProgrammerView(viewsets.ModelViewSet):
    queryset = Programmers.objects.all()
    serializer_class = ProgrammerSerializer
