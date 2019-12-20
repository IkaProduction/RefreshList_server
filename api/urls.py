from .views import TodoViewSet, LabelViewSet, UserViewSet
from rest_framework import routers

urlpatterns = []

router = routers.DefaultRouter()
router.register('todos', TodoViewSet)
router.register('labels', LabelViewSet)
router.register('users', UserViewSet)
