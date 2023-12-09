from django.urls import path
from .views import Register ,Login ,LogOut 
urlpatterns = [
    path("register",Register.as_view()),
    path("login",Login.as_view()),
    path("logout",LogOut.as_view()),
]