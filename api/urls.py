from django.urls import path
from .views import TodoViewSet, LabelViewSet
from rest_framework import routers

urlpatterns = [
]

router = routers.SimpleRouter()
router.register('todos', TodoViewSet)
router.register('labels', LabelViewSet)

# todo: user関連のSerializer設定
# router.register('users', UserViewSet)
