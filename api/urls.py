from django.urls import path
from .views import ListTodo, DetailTodo, ListLabel

urlpatterns = [
    path('todo/<int:pk>/', DetailTodo.as_view()),
    path('todo/', ListTodo.as_view()),
    path('label/', ListLabel.as_view()),
]
