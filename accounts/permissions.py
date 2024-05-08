from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOwnerOrReadOnly(BasePermission):
    """
    Custom permission to only allow owners of an object to edit or delete it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request, so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the object.
        return obj.user == request.user
    


class IsManagerOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        # Read permissions are allowed to any request.
        if request.method in SAFE_METHODS:
            return True

        # Write permissions are only allowed to managers.
        return request.user.is_manager


class IsRequestOwnerOrManager(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Allow the request if the user is the owner of the join request or a manager.
        return request.user == obj.user or request.user.is_manager