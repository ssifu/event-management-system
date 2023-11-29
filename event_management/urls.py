from . import views
from django.urls import path


urlpatterns = [
    path("signup", views.SignupPageView.as_view(), name="signup"),
    path("login", views.LoginPageView.as_view(), name="login"),
    path("home/<str:username>", views.HomePageView.as_view(), name="home"),
    path("event-registration/<int:event_id>",
         views.EventRegistrationView.as_view(), name="event_registration"),
    path("logout", views.LogoutView.as_view(), name="logout")
]
