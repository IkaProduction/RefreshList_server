from django.urls import path
from . import views

from rest_framework import routers
from .virewset import TodoViewSet

urlpatterns = [
    path('', views.todo_list, name='todo_list'),
]

router = routers.DefaultRouter()
router.register('todos', TodoViewSet)
