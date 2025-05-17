from rest_framework.permissions import BasePermission

class isOwnerOrSuperuser(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.owner or request.user.is_superuser


