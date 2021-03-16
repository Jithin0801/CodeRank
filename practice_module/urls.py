from django.urls import path
from . import views

urlpatterns = [
    path("practice/", views.PracticePage, name="PracticePage"),
    path("practice/<slug:maintopic>/<slug:subtopic>/challenges", views.ViewChallenges, name="ViewChallenges"),
]
