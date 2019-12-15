from rest_framework import serializers
from .models import Todo
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username')


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('user_id', 'title', 'important', 'memo')
