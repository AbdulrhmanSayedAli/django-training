from rest_framework.permissions import BasePermission , SAFE_METHODS
from artists.models import Artist
from rest_framework.exceptions import APIException
from rest_framework import status
class IsAuthenticatedorReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return not request.user.is_anonymous

class IsSuperUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_superuser

class IsSameUserOrReadOnly (BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj == request.user



class NotSameUser(APIException):
    status_code = status.HTTP_403_FORBIDDEN
    default_detail = "you must be an artist to do this request"


class IsTheUserArtistOrReadOnly (BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        try:
            artist = request.user.artist
        except  Artist.DoesNotExist:
             raise NotSameUser()
        return True

