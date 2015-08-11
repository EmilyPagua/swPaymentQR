from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from core.models import ToDo, TypeCard, Card


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','first_name','last_name','email')
        write_only_fields = ('password')


class UserPerfilSerializer(ModelSerializer):
    user =  UserSerializer(many=False, read_only=True)

    class Meta:
        model = TypeCard
        fields = ('id','user','code','is_company')


class ToDoSerializer(ModelSerializer):
    propietario =  UserSerializer(many=False, read_only=True)
    class Meta:
        model = ToDo
        fields = ('id','fecha_inicio','fecha_finalizacion','todo','hecho','propietario')

class ToDoHyperSerializer(HyperlinkedModelSerializer):
    propietario = serializers.HyperlinkedRelatedField(
        view_name='usuario',
        lookup_field='id',
        read_only=True
    )
    class Meta:
        model = ToDo
        fields = ('id','fecha_inicio','fecha_finalizacion','todo','hecho','propietario')


class TypeCardSerializer(ModelSerializer):
    class Meta:
        model = TypeCard
        fields = ('id','name')


class CardSerializer(ModelSerializer):
    owner =  UserSerializer(many=False, read_only=True)
    class Meta:
        model = Card
        fields = ('id','owner','number_card','name_card','expiration_year','available')


class CardHyperSerializer(HyperlinkedModelSerializer):
    owner = serializers.HyperlinkedRelatedField(
        view_name='card',
        lookup_field='id',
        read_only=True
    )
    class Meta:
        model = Card
        fields = ('id','type_card','owner','number_card','name_card','expiration_year')