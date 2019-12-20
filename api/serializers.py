from rest_framework import serializers
from todolist.models import Todo, Label
from django.contrib.auth import get_user_model


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
        model = get_user_model()
        fields = ('email', 'username')
