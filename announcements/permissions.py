from django.core.exceptions import PermissionDenied
from rest_framework.permissions import BasePermission

class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Check if the request method is safe (GET, HEAD, OPTIONS)
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True

        # If not a safe method, check if the user is the owner of the announcement
        return obj.owner == request.user


def user_is_employer(function):

    def wrap(request, *args, **kwargs):   

        if request.user.role == 'employer':
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied

    return wrap



def user_is_employee(function):

    def wrap(request, *args, **kwargs):    

        if request.user.role == 'employee':
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied

    return wrap

