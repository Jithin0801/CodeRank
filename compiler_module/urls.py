from django.urls import path
from . import views

urlpatterns = [
    path("practice/<slug:maintopic>/<slug:subtopic>/<slug:problem>/compiler",
         views.Compiler, name="Compiler"),
    path("practice/<slug:maintopic>/<slug:subtopic>/<slug:problem>/submission",
         views.Submission, name="Submission"),
    path("practice/<slug:maintopic>/<slug:subtopic>/<slug:problem>/discussion",
         views.Discussion, name="Discussion"),
    path("practice/<slug:maintopic>/<slug:subtopic>/<slug:problem>/leaderboard",
         views.LeaderBoard, name="LeaderBoard")           
]
