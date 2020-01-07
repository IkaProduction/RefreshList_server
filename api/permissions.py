from rest_framework import permissions


class IsOwnerOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user_id == request.user  # NOTE:レコードのuser_idとリクエストしているuserが同一であるか確認。
