from django.urls import path
from . import views

urlpatterns = [
    path("compete/upcoming", views.UpcomingPage, name="CompeteUpcoming"),
    path("compete/previous", views.PreviousPage, name="CompetePrevious"),
    path("compete/registered", views.RigsteredPage, name="CompeteRegistered"),
    path("compete/ongoing", views.OngoingPage, name="CompeteOngoing"),
    path("compete/<slug:competitionslug>/register",
         views.ViewCompetitionDetails, name="RegisterCompetition"),
    path("compete/<slug:competitionslug>/start_test",
         views.AssessmentStartPage, name="AssessmentStartPage"),
    path("compete/<slug:competitionslug>/question_list",
         views.AssessmentListPage, name="AssessmentListPage")
]
