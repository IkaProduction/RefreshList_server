from django.db import models
from django.contrib.auth import get_user_model


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
        blank=True,
    )
    memo = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    labels = models.ManyToManyField(
        Label,
        blank=True,
    )
