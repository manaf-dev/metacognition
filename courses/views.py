from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, "courses/home.html")


def all_courses(request):
    return render(request, 'courses/all_courses.html')


def self_quiz(request):
    return render(request, 'courses/quiz.html')