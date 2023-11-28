from . import views
from django.urls import path


urlpatterns = [
    path("signup", views.SignupPage, name="signup"),
    path("login", views.LoginPage, name="login"),
    path("home", views.HomePage, name="home"),
]
