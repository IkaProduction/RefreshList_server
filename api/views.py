from rest_framework import generics
from todolist.models import Todo, Label
from .serializers import TodoSerializer, LabelSerializer


class ListTodo(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class DetailTodo(generics.RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class ListLabel(generics.ListAPIView):
    queryset = Label.objects.all()
    serializer_class = LabelSerializer
