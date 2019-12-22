from django.conf.urls import include
from django.urls import path
from .views import TodoViewSet, LabelViewSet, UserViewSet, UserCreateView, CheckView, LoginView
from rest_framework import routers

router = routers.DefaultRouter()

router.register('todos', TodoViewSet)
router.register('labels', LabelViewSet)
router.register('users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('sign-up/', UserCreateView.as_view()),  # NOTE: ユーザー作成
    path('login/', LoginView.as_view()),  # NOTE: ユーザー認証をしてセッションIDを発行
    path('user-check/', CheckView.as_view()),  # NOTE: セッションとユーザー確認用
]
