from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("scorecards/", views.scorecards, name="scorecards"),
    path("userscore/", views.userscore, name="userscore"),
    path("rules/", views.rules, name="rules"),
    path("reset_all/", views.reset_all, name="reset_all"),
]
