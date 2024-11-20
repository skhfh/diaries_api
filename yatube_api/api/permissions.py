from rest_framework import permissions


class ReadOnlyOrAuthor(permissions.BasePermission):
    """Пермишен:
    GET - для всех
    POST - создание нового объекта для аутентифицированных
    PUT / PATCH / DELETE - для автора объекта
    """
    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user
        )
