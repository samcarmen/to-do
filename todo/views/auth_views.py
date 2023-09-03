import requests
from django.contrib.auth import get_user_model, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from todo_backend.settings import (
    BASE_URL,
    GOOGLE_CLIENT_ID,
    GOOGLE_CLIENT_SECRET,
)

from ..models import Todo

User = get_user_model()


def google_login(request):
    google_oauth2_url = "https://accounts.google.com/o/oauth2/v2/auth"
    redirect_uri = f"{BASE_URL}todo/callback/"
    scope = (
        "https://www.googleapis.com/auth/userinfo.email "
        "https://www.googleapis.com/auth/userinfo.profile"
    )
    response_type = "code"

    authorization_url = (
        f"{google_oauth2_url}?client_id={GOOGLE_CLIENT_ID}"
        f"&redirect_uri={redirect_uri}"
        f"&scope={scope}&response_type={response_type}"
    )

    return redirect(authorization_url)


@api_view(["GET"])
def google_callback(request):
    auth_code = request.GET.get("code", None)
    if auth_code is None:
        return redirect("login_failed_view")

    data = {
        "code": auth_code,
        "client_id": GOOGLE_CLIENT_ID,
        "client_secret": GOOGLE_CLIENT_SECRET,
        "redirect_uri": f"{BASE_URL}todo/callback/",
        "grant_type": "authorization_code",
    }
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    response = requests.post(
        "https://oauth2.googleapis.com/token", data=data, headers=headers
    )

    token_data = response.json()
    if "error" in token_data:
        return redirect("login_failed_view")

    access_token = token_data["access_token"]

    # Fetching user information
    user_info_response = requests.get(
        "https://www.googleapis.com/oauth2/v2/userinfo",
        headers={"Authorization": f"Bearer {access_token}"},
    )
    user_info = user_info_response.json()

    # Try to find existing user by email
    user, created = User.objects.get_or_create(email=user_info["email"])

    if created:
        user.username = user_info["email"]
        user.first_name = user_info.get("given_name", "")
        user.last_name = user_info.get("family_name", "")
        user.set_password(User.objects.make_random_password())
        user.save()

    # Log the user in
    login(request, user, backend="django.contrib.auth.backends.ModelBackend")

    # Generate or get a DRF token for the user
    drf_token, created = Token.objects.get_or_create(user=user)

    request.session["drf_token"] = drf_token.key

    return redirect("home")


def login_failed_view(request):
    return render(request, "login_failed.html")


@login_required
def home(request):
    user = request.user
    todos = Todo.objects.filter(user=user).order_by("-created_at")
    # Displaying the drf token to ease testing on Postman
    drf_token = request.session.get("drf_token", "No token found.")
    return render(
        request,
        "home.html",
        {"todos": todos, "drf_token": drf_token},
    )
