from django.urls import path
from .views import AlbumView , ManualAlbumView

urlpatterns = [
    path("",AlbumView.as_view()),
    path("manual/",ManualAlbumView.as_view())
]