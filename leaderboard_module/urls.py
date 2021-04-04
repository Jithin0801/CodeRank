from django.urls import path
from . import views

urlpatterns = [
    path("leaderboard/", views.LeaderBoard, name="LeaderBoardPage"),
]
