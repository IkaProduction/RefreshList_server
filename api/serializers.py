from rest_framework import serializers
from todolist.models import Todo, Label
from users.models import User


class LabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Label
        fields = ('id', 'user_id', 'title', 'coler_code')
        read_only_fields = ['id']


class TodoSerializer(serializers.ModelSerializer):
    # NOTE:get専用主キー指定
    # labels = serializers.StringRelatedField()
    # NOTE:post可能主キー指定
    # labels = serializers.PrimaryKeyRelatedField(queryset=Label.objects.filter(), many=True)
    # NOTE:ネスト表示だがgetしか出来ない
    labels = LabelSerializer(many=True, read_only=True)

    class Meta:
        model = Todo
        fields = ('id', 'user_id', 'title', 'finished_flag', 'deadline', 'important', 'memo', 'labels')
        read_only_fields = ['id']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'username', 'password')
        extra_kwargs = {
            'password': {'write_only': True},  # NOTE:passwordは書き込みのみを許可
        }

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)  # NOTE:入力データを引数にuser作成を実行
