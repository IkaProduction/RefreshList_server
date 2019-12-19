from django.urls import path
from .views import TodoViewSet, LabelViewSet
from rest_framework import routers

urlpatterns = []

router = routers.SimpleRouter()
router.register('todos', TodoViewSet)
router.register('labels', LabelViewSet)

# todo: user関連のrouter設定を一旦オミット。ユーザー登録、ログイン、ログアウトの実装に併せて修正か削除します。
# router.register('users', UserViewSet)
