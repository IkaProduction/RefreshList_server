from todolist.models import Todo, Label
from django.contrib.auth import get_user_model
from .serializers import TodoSerializer, LabelSerializer, UserSerializer
from rest_framework import viewsets, generics
from rest_framework.authentication import SessionAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import authenticate, login, logout
from django_filters.rest_framework import DjangoFilterBackend


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


class TodoListView(generics.ListAPIView):
    serializer_class = TodoSerializer
    queryset = Todo.objects.filter()
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['user_id']
