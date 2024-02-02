from django.urls import path
from . import views

urlpatterns = [
    path("signup_new_user/", views.signup_new_user, name="signup_new_user"),
]
