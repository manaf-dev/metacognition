from django.shortcuts import render, redirect
from .forms import SignupForm


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            print("Account created successfully")
            return redirect("login")
        else:
            print("Error creating account")
    return render(request, "accounts/signup.html")
