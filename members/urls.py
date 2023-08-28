from django.urls import path

from . import views

urlpatterns = [
    path("login_user", views.login_user, name="login"),
    path("logout_user", views.logout_user, name="logout"),
    path("register_user", views.register_user, name="register"),
    path("user_profile", views.user_profile, name="profile"),
]