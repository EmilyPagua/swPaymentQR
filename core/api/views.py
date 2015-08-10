from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from core.api.serializers import UserSerializer, ToDoSerializer, ToDoHyperSerializer
from core.models import ToDo


class HolaMundo(APIView):
    def get(self,request,nombre,fromat=None):
        return Response({'mensaje':'Hola ' +nombre +' Mundo de Django Rest Framwork'})

hola_mundo = HolaMundo.as_view()


class ToDoView(APIView):
    serializer_class = ToDoSerializer

    def get(self,request,id=None, format=None):
        todos = ToDo.objects.all()
        response = self.serializer_class(todos,many=True, context={'request': request})
        return Response(response.data)

    def post(self,request,format=None):
        todo = self.serializer_class(data=request.DATA, context={'request': request})
        print request.DATA
        if todo.is_valid():
            print 'valido'
            obj = todo.object
            obj.propietario = request.User
            obj.save()
            resp = self.serializer_class(obj,many=False,context={'request': request})
            return Response(resp.data)
        else:
            print todo.errors

todoview = ToDoView.as_view()

class UserViewset(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = 'id'

user_list = UserViewset.as_view({'get':'list'})
user_detail = UserViewset.as_view({'get':'retrieve'})

class ToDoViewSet(viewsets.ModelViewSet):
    serializer_class = ToDoSerializer
    queryset = ToDo.objects.all()
    lookup_field = 'id'

    def list(self, request, *args, **kwargs):
        print request.user
        return super(ToDoViewSet, self).list(request,*args,**kwargs)


todo_list = ToDoViewSet.as_view({'get':'list'})
todo_detail = ToDoViewSet.as_view({'get':'retrieve'})

