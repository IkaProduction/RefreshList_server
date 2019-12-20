from rest_framework import serializers
from todolist.models import Todo, Label
from users.models import User


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'user_id', 'title', 'finished_flag', 'deadline', 'important', 'memo')
        read_only_fields = ['id', 'user_id']


class LabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Label
        fields = ('title', 'coler_code')
        read_only_fields = ['User_id']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'username', 'password')
        extra_kwargs = {
            'password': {'write_only': True},  # 'password'は読み取り専用
        }

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)  # 入力データを引数にuser作成を実行
