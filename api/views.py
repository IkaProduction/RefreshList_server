from todolist.models import Todo, Label
from django.contrib.auth import get_user_model, authenticate, login, logout
from .serializers import TodoSerializer, LabelSerializer, UserSerializer
from rest_framework import viewsets, generics
from rest_framework.authentication import SessionAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from .permission import IsUserOnly


class TodoViewSet(viewsets.ModelViewSet):
    permission_classes = (IsUserOnly, )  # NOTE:todoのユーザーIDとログインユーザーが一致した場合のみrequestを受け付けるパーミッション
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


class CheckView(APIView):  # NOTE:セッション確認
    authentication_classes = (SessionAuthentication, )
    permission_classes = (IsAuthenticated, )  # NOTE:認証済みユーザーのみアクセス許可

    def get(self, request, format=None):
        content = {'user': str(request.user), 'auth': str(request.auth)}
        return Response(content)


class LoginView(APIView):  # NOTE:ユーザー認証が完了するとセッションIDが返答される
    permission_classes = (AllowAny, )  # NOTE:認証不要

    def post(self, request):
        email = request.data['email']
        password = request.data['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return Response({'session': request.session.session_key})


class LogoutView(APIView):
    permission_classes = (AllowAny, )  # NOTE:認証不要

    def get(self, request):
        logout(request)
        return Response({'session': 'logout'})
