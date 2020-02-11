from django.contrib.auth import get_user_model
from django.db import models


class Label(models.Model):
    user_id = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=16)
    color_code = models.CharField(
        max_length=7,
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(
        blank=True,
        null=True,
    )


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
    important = models.IntegerField(
        choices=(
            (0, 'Nothing'),
            (1, 'Low'),
            (2, 'Medium'),
            (3, 'High'),
        ),
        default=0,
    )
    memo = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    labels = models.ManyToManyField(
        Label,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(
        blank=True,
        null=True,
    )
