from rest_framework.permissions import BasePermission


class IsManager(BasePermission):
    ''' Custom Permission to check whether the user is a manager or not  '''
    def has_permission(self, request, view):
        return bool( (request.user.roles == "manager") or (request.user.roles == "admin") or (request.user.is_staff))
