from django.urls import path
from . import views

urlpatterns = [
    path("tutorials/", views.MainTopicPage, name="TutorialPage"),
    path("tutorials/<slug:maintopic>",
         views.SubTopicPage, name="SubTopicPage"),
    path("tutorials/<slug:maintopic>/<slug:subtopic>/",
         views.TutorialSubTopicPage, name="TutorialSubTopicPage"),
    path("tutorials/<slug:maintopic>/<slug:subtopic>/<slug:tutorialsubtopic>",
         views.ViewTutorialPage, name="ViewTutorialPage"),


]
