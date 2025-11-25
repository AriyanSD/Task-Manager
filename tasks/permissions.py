from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Object-level permission: only owner can edit/delete.
    Read is allowed to authenticated users (or make it allow any if you want public visibility).
    """

    def has_permission(self, request, view):
        # require authentication for unsafe methods
        if request.method in permissions.SAFE_METHODS:
            return request.user and request.user.is_authenticated
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user
