from rest_framework import serializers
from todolist.models import Todo, Label
from users.models import User


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'user_id', 'title', 'finished_flag', 'deadline', 'important', 'memo')


class LabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Label
        fields = ('user_id', 'title', 'coler_code')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')