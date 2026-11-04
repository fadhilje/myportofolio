from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsPortofolioOwnerOrReadOnly(BasePermission):
    message = "Only the portofolio owner can change projects."

    def has_permission(self, request, view):
        return (
            request.mehtod in SAFE_METHODS
            or request.user.is_superuser
        )