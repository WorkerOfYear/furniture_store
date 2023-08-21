from rest_framework import permissions


class IsSuperUser(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        
        return obj.username == request.is_superuser