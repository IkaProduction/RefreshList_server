from django.contrib.auth import authenticate, get_user_model, login, logout
from rest_framework import generics, viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import TodoSerializer, LabelSerializer, UserSerializer
from todolist.models import Todo, Label


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def get_queryset(self):
        return Todo.objects.filter(user_id=self.request.user)  # NOTE:ログインユーザーのIDでフィルタリング表示


class TodoListView(viewsets.ModelViewSet):  # FIXME: todo操作の確認用
    permission_classes = (AllowAny, )  # NOTE:認証不要
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    filter_fields = ['user_id']  # NOTE:URLのqueryでフィルタリング出来る項目


class LabelViewSet(viewsets.ModelViewSet):
    queryset = Label.objects.all()
    serializer_class = LabelSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class UserCreateView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny, )  # NOTE:認証不要


# NOTE:セッション確認
class CheckView(APIView):
    authentication_classes = (SessionAuthentication, )
    permission_classes = (IsAuthenticated, )  # NOTE:認証済みユーザーのみアクセス許可

    def get(self, request, format=None):
        content = {'user': str(request.user), 'auth': str(request.auth)}
        return Response(content)


class LoginView(APIView):
    permission_classes = (AllowAny, )  # NOTE:認証不要

    def post(self, request):
        email = request.data['email']
        password = request.data['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return Response({"session": request.session.session_key})  # NOTE:ユーザー認証が完了するとセッションIDが返答される


class LogoutView(APIView):
    permission_classes = (AllowAny, )  # NOTE:認証不要

    def get(self, request):
        logout(request)
        return Response({"session": 'ログアウトしました。'})
