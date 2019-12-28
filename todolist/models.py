import uuid
from django.db import models
from django.contrib.auth import get_user_model

# class [テーブル名](models.Model):
#     フィールド名 = models.[適切な型]([オプション])


class Todo(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    user = models.ForeignKey(
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
        (0, 'Nothing'),
        (1, 'Low'),
        (2, 'Medium'),
        (3, 'High'),
    )
    important = models.IntegerField(
        choices=IMPORTANT,
        default=0,
    )
    memo = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )


class Label(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=16)
    coler_code = models.CharField(
        max_length=7,
        null=True,
    )


class Todo_Label(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    todo = models.ForeignKey(
        Todo,
        on_delete=models.CASCADE,
    )
    label = models.ForeignKey(
        Label,
        on_delete=models.CASCADE,
    )
