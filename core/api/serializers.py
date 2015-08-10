from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from core.models import ToDo


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','first_name','last_name','email')
        write_only_fields = ('password')

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
