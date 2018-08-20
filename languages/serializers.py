from rest_framework import serializers
from .models import Languages, Paradigms, Programmers

class LanguageSerializer(serializers.HyperlinkedModelSerializer): #ModelSerializer
    class Meta:
        model       = Languages
        fields      = ('id','url','name','paradigm')

class ParadigmSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model       = Paradigms
        fields      = ('id','url','name')

class ProgrammerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model       = Programmers
        fields      = ('id','url','name','languages')