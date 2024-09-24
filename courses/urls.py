from django.urls import path

from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("courses/", views.all_courses, name="all_courses"),
    path("self-test-quiz/", views.self_quiz, name="self_quiz"),
]
