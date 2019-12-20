from rest_framework import serializers
from todolist.models import Todo, Label
from users.models import UserManager
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password


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
        model = get_user_model()
        fields = ('email', 'username', 'password')
        extra_kwargs = {
            'password': {'write_only': True},  # 'password'は読み取り専用
        }

    def create(self, validated_data):
        password = validated_data.get('password')  # 入力データから'password'の値を読み取り
        validated_data['password'] = make_password(password)  # ハッシュ化した'password'を格納
        return UserManager.create_user(self, **validated_data)  # 入力データを引数にuser作成を実行
