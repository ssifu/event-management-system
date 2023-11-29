from asyncio.windows_events import NULL
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import get_object_or_404
from django.db.models import Count

from django.urls import reverse

from .models import Event, Users, UserEventRegistration

# Create your views here.


def SignupPage(request):
    if request.method == "POST":
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]

        if Users.objects.filter(username=username).exists():
            messages.error(request, "Username already exists",
                           extra_tags="duplicate_username")
            return redirect("/signup")

        new_user = Users(username=username, email=email,
                         password=password, first_name=firstname, last_name=lastname)

        new_user.save()

        return redirect("/login")

    return render(request, "event_management/signup_form.html")


def LoginPage(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        try:
            user = Users.objects.get(username=username)
        except Users.DoesNotExist:
            messages.error(
                request, "User with this username does not exist", extra_tags="user_not_found")
            return redirect("login")

        if password != user.password:
            messages.error(request, "Password is incorrect",
                           extra_tags="incorrect_password")
            return redirect("login")
        else:
            request.session['username'] = username
            home_url = reverse('home', kwargs={'username': username})
            return redirect(home_url)

    return render(request, "event_management/login_form.html")


def LogoutPage(request):
    request.session.clear()
    return redirect("login")


def HomePage(request, username):
    if 'username' in request.session and request.session['username'] == username:
        try:
            user = Users.objects.get(username=username)

            # Retrieve registered events for the user
            registered_events = UserEventRegistration.objects.filter(
                user=user).values_list('event_id', flat=True)
            print(f"registered_events: {registered_events}\n\n")

            # Get all events
            all_events = Event.objects.annotate(
                registration_count=Count('usereventregistration')).all()

            print(f"all_events: {all_events}\n\n")

            # Separate registered and unregistered events
            registered_event_ids = set(registered_events)

            print(f"registered_event_ids: {registered_event_ids}\n\n")
            registered_events = [
                event for event in all_events if event.id in registered_event_ids]

            print(f"registered_events: {registered_events}\n\n")
            unregistered_events = [
                event for event in all_events if event.id not in registered_event_ids]

            print(f"unregistered_events: {unregistered_events}\n\n")

            fullname = (user.first_name or "") + " " + (user.last_name or "")
            formatted_registered_events = [
                {"event": event, "formatted_datetime": event.formatted_datetime()} for event in registered_events]
            formatted_unregistered_events = [
                {"event": event, "formatted_datetime": event.formatted_datetime()} for event in unregistered_events]

            return render(request, "event_management/home.html", {
                "user_fullname": fullname,
                "registered_events": formatted_registered_events,
                "unregistered_events": formatted_unregistered_events,
            })

        except Users.DoesNotExist:
            # Handle the case when the user does not exist
            return HttpResponse("User not found", status=404)
    else:
        return redirect("login")


def EventRegistration(request, event_id):
    try:
        user = Users.objects.get(username=request.session['username'])
        event = get_object_or_404(Event, id=event_id)
    except Users.DoesNotExist:
        # Handle the case when the user does not exist
        return HttpResponse("User not found", status=404)
    except Event.DoesNotExist:
        # Handle the case when the event does not exist
        return HttpResponse("Event not found", status=404)

    new_registered_event = UserEventRegistration(user=user, event=event)
    new_registered_event.save()

    return redirect(reverse('home', kwargs={'username': request.session['username']}))
