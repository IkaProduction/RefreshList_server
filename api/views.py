from todolist.models import Todo, Label
from .serializers import TodoSerializer, LabelSerializer
from rest_framework import viewsets


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class LabelViewSet(viewsets.ModelViewSet):
    queryset = Label.objects.all()
    serializer_class = LabelSerializer


# todo: user関連のSerializer設定を一旦オミット。ユーザー登録、ログイン、ログアウトの実装に併せて修正か削除します。
# from django.contrib.auth import get_user_model
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer
