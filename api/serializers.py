from rest_framework import serializers
from todolist.models import Todo, Label
from django.contrib.auth import get_user_model


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'user_id', 'title', 'finished_flag', 'deadline', 'important', 'memo')
        read_only_fields = ('id', 'user_id')


class LabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Label
        fields = ('title', 'coler_code')
        read_only_fields = ('User_id')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'email', 'username', 'password')
        write_only_fields = ('password')
        read_only_fields = ('id',)
