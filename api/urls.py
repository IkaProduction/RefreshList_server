from django.conf.urls import include
from django.urls import path
from .views import TodoViewSet, LabelViewSet, UserViewSet, UserCreateView
from rest_framework import routers

router = routers.DefaultRouter()

router.register('todos', TodoViewSet)
router.register('labels', LabelViewSet)
router.register('users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('sign_up/', UserCreateView.as_view()),
]
