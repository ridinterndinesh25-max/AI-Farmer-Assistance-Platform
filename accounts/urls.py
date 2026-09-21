from django.urls import path
from . import views


urlpatterns = [

    path(
        "register/",
        views.register,
        name="register"
    ),

    path(
        "login/",
        views.user_login,
        name="login"
    ),

    path(
        "logout/",
        views.user_logout,
        name="logout"
    ),

    path(
        "profile/",
        views.profile,
        name="profile"
    ),

    path(
        "profile/history/",
        views.profile_history,
        name="profile_history"
    ),

    path(
        "farmer/edit/<int:user_id>/",
        views.edit_farmer,
        name="edit_farmer"
    ),

]