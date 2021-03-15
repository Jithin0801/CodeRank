from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.DevHomePage, name="DevHome"),
    path("practice/", views.PracticePage, name="PracticePage")
]
