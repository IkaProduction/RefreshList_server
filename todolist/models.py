from django.db import models
from django.contrib.auth import get_user_model

# class [テーブル名](models.Model):
#     フィールド名 = models.[適切な型]([オプション])


class Todo(models.Model):
    user_id = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=32)
    finished_flag = models.BooleanField(default=False)
    deadline = models.TimeField(
        null=True,
        blank=True,
    )
    IMPORTANT = (
        ('0', 'Nothing'),
        ('1', 'Low'),
        ('2', 'Medium'),
        ('3', 'High'),
    )
    important = models.CharField(
        max_length=1,
        choices=IMPORTANT,
        default=0,
    )
    memo = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )


class Label(models.Model):
    user_id = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=16)
    coler_code = models.CharField(
        max_length=7,
        null=True,
    )


class Todo_Label(models.Model):
    todo_id = models.ForeignKey(
        Todo,
        on_delete=models.CASCADE,
    )
    label_id = models.ForeignKey(
        Label,
        on_delete=models.CASCADE,
    )
