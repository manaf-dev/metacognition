from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            print("Account created successfully")
            return redirect("home")
        else:
            print("Error creating account")
    return render(request, "accounts/signup.html")
