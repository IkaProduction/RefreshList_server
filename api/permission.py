from rest_framework import permissions


class IsUserOnly(permissions.BasePermission):
    """
    todoを作成したユーザーだけが閲覧、変更出来るようにしたい。
    """
    def has_object_permission(self, request, view, obj):  #FIXME:新規追加と変更で別のuseridを指定出来る
        return obj.user_id == request.user
