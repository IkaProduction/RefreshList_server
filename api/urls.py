from django.conf.urls import include
from django.urls import path
from .views import TodoViewSet, LabelViewSet, UserViewSet, UserCreateView, CheckView, SessionView
from rest_framework import routers

router = routers.DefaultRouter()

router.register('todos', TodoViewSet)
router.register('labels', LabelViewSet)
router.register('users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('sign-up/', UserCreateView.as_view()),
    path('login-check/', CheckView.as_view()),  # FIXME: ログインチェック用
    path('login-session/', SessionView.as_view()),  # FIXME: ユーザー認証をしてセッションIDを発行
