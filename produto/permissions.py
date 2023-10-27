from rest_framework import permissions

class AllowAnonymousGet(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True  # Permite POST não autenticado
        return request.user.is_authenticated
