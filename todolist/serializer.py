from rest_framework import serializers
from .models import Todo


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('name', 'mail')


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('user_id', 'title', 'important', 'memo')
