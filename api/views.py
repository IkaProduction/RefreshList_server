from todolist.models import Todo, Label
from django.contrib.auth import get_user_model
from .serializers import TodoSerializer, LabelSerializer, UserSerializer
from rest_framework import viewsets, generics
from rest_framework.authentication import SessionAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate, login


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class LabelViewSet(viewsets.ModelViewSet):
    queryset = Label.objects.all()
    serializer_class = LabelSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class UserCreateView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class CheckView(APIView):  # NOTE:セッション確認
    authentication_classes = (SessionAuthentication, )

    def get(self, request, format=None):
        content = {'user': str(request.user), 'auth': str(request.auth)}
        return Response(content)


class SessionView(APIView):  # NOTE:ユーザー認証が完了するとセッションIDが返答される

    def post(self, request):
        email = request.data['email']
        password = request.data['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return Response({'session': request.session.session_key})

# TODO: ログアウト処理を書く
