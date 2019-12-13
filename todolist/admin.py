from django.contrib import admin
from .models import Todo, Label, Todo_Label

admin.site.register(Todo)
admin.site.register(Label)
admin.site.register(Todo_Label)
