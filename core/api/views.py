from django.contrib.auth.models import User
from rest_framework import viewsets
from core.api.serializers import UserSerializer, ToDoSerializer, TypeCardSerializer, CardSerializer
from core.models import ToDo, TypeCard, Card


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


class TypeCardViewSet(viewsets.ModelViewSet):
    serializer_class = TypeCardSerializer
    queryset = TypeCard.objects.all()
    lookup_field = 'id'

    def list(self, request, *args, **kwargs):
        print request.user
        return super(TypeCardViewSet, self).list(request,*args,**kwargs)

typecard_list = TypeCardViewSet.as_view({'get':'list'})
typecard_detail = TypeCardViewSet.as_view({'get':'retrieve'})


class CardViewset(viewsets.ModelViewSet):
    serializer_class = CardSerializer
    queryset = User.objects.all()
    lookup_field = 'id'

card_list = CardViewset.as_view({'get':'list'})
card_detail = CardViewset.as_view({'get':'retrieve'})




