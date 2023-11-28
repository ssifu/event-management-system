from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login

# Create your views here.


def SignupPage(request):
    if request.method == "POST":
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists", extra_tags="duplicate_username")
            return redirect("/signup")

        new_user = User.objects.create_user(username, email, password)

        new_user.first_name = firstname
        new_user.last_name = lastname

        new_user.save()

        messages.success(request, "User creation successful!")

        return redirect("/login")

    return render(request, "event_management/signup_form.html")


def LoginPage(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return render(request, "event_management/home.html", {"username": user.get_username})
        else:
            messages.error(request, "Wrong Username or Password")
            return redirect("/login")

    return render(request, "event_management/login_form.html")


def HomePage(request):
    return render(request, "event_management/home.html")
