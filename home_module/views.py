from login_module.models import Profile
from practice_module.models import PracticeMainTopic, PracticeSubTopic
from blog_module.models import BlogModel
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import compete_module.models
import tutorial_module.models


@login_required
def DevHomePage(request):
    userid = request.user.id
    blogsqueryset = BlogModel.objects.all()
    competitionqueryset = compete_module.models.CompeteModel.objects.filter(status_id = 1)
    registeredcompetitionsquerylist = list(
        compete_module.models.RegisteredUserCompete.objects.all().values())
    registeredcompetitionids = []
    for registeredcompetitions in registeredcompetitionsquerylist:
        if userid == registeredcompetitions['user_id']:
            registeredcompetitionids.append(
                registeredcompetitions['competition_id'])

    tutorialsqueryset = tutorial_module.models.TutorialContent.objects.all()
    practicemaintopicqueryset = PracticeMainTopic.objects.all()
    practicesubtopicquertset = PracticeSubTopic.objects.all()
    profilequeryset = Profile.objects.all().order_by("-score")

    context = {
        "title": "CodeRank - Home",
        "pagetitle": "home",
        "blogsqueryset":blogsqueryset,
        "competitionqueryset": competitionqueryset,
        "tutorialsqueryset":tutorialsqueryset,
        "practicemaintopicqueryset": practicemaintopicqueryset,
        "subtopicquertset": practicesubtopicquertset,
        "registeredcompetitionids": registeredcompetitionids,
        "profilelist": profilequeryset

    }
    return render(request, "home_module/home.html", context)
