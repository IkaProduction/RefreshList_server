# django_restflamework
from rest_framework import viewsets
from .models import Todo
from .serializer import TodoSerializer, UserSerializer

# ユーザー関係
from django.contrib.auth import get_user_model


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
