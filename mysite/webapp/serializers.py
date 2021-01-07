from django.contrib.auth.models import User
from .models import *
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'email', 'groups']


class SymbolSerializer(serializers.ModelSerializer):
    # https://stackoverflow.com/questions/28200485/foreign-key-value-in-django-rest-framework
    name = serializers.CharField(read_only=True)

    class Meta:
        model = Symbol
        fields = ('id', 'name')


class TradeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Trade
        fields = '__all__'


class EntrySerializer(serializers.ModelSerializer):
    symbol = serializers.CharField(source="symbol.name", read_only=True)

    class Meta:
        model = Entry
        fields = '__all__'