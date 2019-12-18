from django.urls import path
from . import views

from rest_framework import routers
from .virewset import TodoViewSet, UserViewSet

# todo: Defaultのviewの連結なので削除
urlpatterns = [
    path('', views.todo_list, name='todo_list'),
]

# todo: DRF関連の不要な設定
# router = routers.DefaultRouter()
# router.register('todos', TodoViewSet)
# router.register('users', UserViewSet)
