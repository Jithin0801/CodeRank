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
         views.LeaderBoard, name="LeaderBoard"),
    path("practice/<slug:maintopic>/<slug:subtopic>/<slug:problem>/compiler/compile/",
         views.Compile, name="Compile"),
    path("practice/<slug:maintopic>/<slug:subtopic>/<slug:problem>/compiler/submit/",
         views.SubmitCode, name="SubmitCode"),
    path("practice/<slug:maintopic>/<slug:subtopic>/<slug:problemslug>/submission/<slug:problemresult>/",
         views.SubmissionDetails, name="SubmissionDetails"),
    path("test/<slug:problem>/compiler/",
         views.TestCompiler, name="TestCompiler"),
    path("test/<slug:problem>/compiler/compile/",
         views.TestCompile, name="TestCompile"),
    path("test/<slug:problem>/compiler/submit/",
         views.TestSubmitCode, name="TestSubmitCode"),
]
