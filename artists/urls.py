from django.urls import path
from .views import ArtistsView


urlpatterns = [
    path("",ArtistsView.as_view())
]