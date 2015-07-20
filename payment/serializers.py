__author__ = 'epagua'
from django.forms import widgets
from rest_framework import serializers
from payment.models import TypeUser
from django.contrib.auth.models import User


class TypeUserSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    owner = serializers.ReadOnlyField(source='owner.username')

    def create(self, validated_data):
        return TypeUser.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.owner = validated_data.get('owner', instance.owner)
        instance.save()
        return instance

class UserSerializer(serializers.ModelSerializer):
    typeuser = serializers.PrimaryKeyRelatedField(many=True, queryset=TypeUser.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'fktypeuser')
