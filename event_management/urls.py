from . import views
from django.urls import path


urlpatterns = [
    path("signup", views.SignupPage, name="signup"),
    path("login", views.LoginPage, name="login"),
    path("home/<str:username>", views.HomePage, name="home"),
    path("event-registration/<int:event_id>",
         views.EventRegistration, name="event_registration"),
    path("logout", views.LogoutPage, name="logout")
]
