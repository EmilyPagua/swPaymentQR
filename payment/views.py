from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import permissions
from payment.serializers import TypeUserSerializer, UserSerializer
from payment.permissions import IsOwnerOrReadOnly
from payment.models import TypeUser



class TypeUserList(generics.ListCreateAPIView):
    queryset = TypeUser.objects.all()
    serializer_class = TypeUserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class TypeUserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TypeUser.objects.all()
    serializer_class = TypeUserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
