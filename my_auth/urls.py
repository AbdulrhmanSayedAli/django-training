from django.urls import path
from .views import LogOutView, LoginView


urlpatterns = [
    path("login/",LoginView.as_view()),
    path("logout/",LogOutView.as_view())
]