from rest_framework import permissions

class AllowAnonymousPost(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST':
            return True  # Permite POST não autenticado
        return request.user.is_authenticated
