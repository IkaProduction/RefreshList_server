from todolist.models import Todo, Label
from .serializers import TodoSerializer, LabelSerializer
from rest_framework import viewsets
from django.contrib.auth import get_user_model


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class LabelViewSet(viewsets.ModelViewSet):
    queryset = Label.objects.all()
    serializer_class = LabelSerializer


# # todo: user関連のSerializer設定
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer
