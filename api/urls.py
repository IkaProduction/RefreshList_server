from django.urls import path
from .views import ListTodo, DetailTodo, ListLabel

urlpatterns = [
    path('todos/<int:pk>/', DetailTodo.as_view()),
    path('todos/', ListTodo.as_view()),
    path('labels/', ListLabel.as_view()),
]
