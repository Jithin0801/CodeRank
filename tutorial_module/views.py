from login_module.models import Profile
from django.contrib.auth.models import User
from tutorial_module.forms import MarkAsReadForm
from tutorial_module.models import TutorialContent, TutorialSubtopic, TutorialSubtopicCompletedStatus
from practice_module.models import PracticeMainTopic, PracticeSubTopic
from django.shortcuts import redirect, render

# Create your views here.


def MainTopicPage(request):
    if request.method == 'GET':
        main_topic = PracticeMainTopic.objects.all()
        sub_topic = PracticeSubTopic.objects.all()
        context = {
            "title": "CodeRank - Tutorials",
            "main": main_topic,
            "pagetitle": "tutorial"
        }
    return render(request, "tutorial_module/maintopics.html", context)


def SubTopicPage(request, maintopic):
    subtopictopicid = PracticeMainTopic.objects.filter(
        slug=maintopic).values_list('id', flat=True)

    maintopictitlequeryset = list(
        PracticeMainTopic.objects.filter(slug=maintopic).values())
    maintopictitle = maintopictitlequeryset[0]['title']
    subtopics = PracticeSubTopic.objects.filter(
        maintopic_id=subtopictopicid[0])
    context = {
        "title": "CodeRank - Tutorials",
        "maintopicslug": maintopic,
        "maintopictitle": maintopictitle,
        "sub": subtopics,
        "pagetitle": "tutorial"
    }
    return render(request, "tutorial_module/subtopics.html", context)


def TutorialSubTopicPage(request, maintopic, subtopic):
    tutorialsubtopicid = PracticeSubTopic.objects.filter(
        slug=subtopic).values_list('id', flat=True)
    subtopictitlequeryset = list(
        PracticeSubTopic.objects.filter(slug=subtopic).values())
    subtopictitle = subtopictitlequeryset[0]['title']
    tutorialsubtopic = TutorialSubtopic.objects.filter(
        subtopic_id=tutorialsubtopicid[0])
    tutorialsubtopiccompletedstatusquerylist = list(TutorialSubtopicCompletedStatus.objects.filter(
        user_id=request.user.id).values_list("tutorialsubtopic_id", flat=True))

    context = {
        "title": "CodeRank - Tutorials",
        "subtopictitle": subtopictitle,
        "maintopicslug": maintopic,
        'subtopicslug': subtopic,
        "tutorialsub": tutorialsubtopic,
        "completedtutorialslist": tutorialsubtopiccompletedstatusquerylist,
        "pagetitle": "tutorial"
    }

    return render(request, "tutorial_module/tutorialsubtopics.html", context)


def ViewTutorialPage(request, maintopic, subtopic, tutorialsubtopic):
    form = MarkAsReadForm()
    tutorialsubtopicqueryset = list(
        TutorialSubtopic.objects.filter(slug=tutorialsubtopic).values())
    tutorialsubtopicid = tutorialsubtopicqueryset[0]["id"]
    tutorialsubtopictitle = tutorialsubtopicqueryset[0]["title"]
    tutorialsubtopiccontent = TutorialContent.objects.filter(
        id=tutorialsubtopicid)
    tutorialsubtopiccompletedstatusquerylist = list(TutorialSubtopicCompletedStatus.objects.filter(
        user_id=request.user.id).values_list("tutorialsubtopic_id", flat=True))

    if request.method == "GET":
        context = {
            "title": "CodeRank - Tutorials",
            "tutorialsubtopictitle": tutorialsubtopictitle,
            "maintopicslug": maintopic,
            'subtopicslug': subtopic,
            "tutorialsubslug": tutorialsubtopic,
            "tutorialsubtopiccontent": tutorialsubtopiccontent,
            "form": form,
            "completedtutorialslist": tutorialsubtopiccompletedstatusquerylist,
            "pagetitle": "tutorial"
        }
    elif request.method == "POST":

        TutorialSubtopicCompletedStatus.objects.create(
            user_id=request.user.id, tutorialsubtopic_id=tutorialsubtopicid, iscompleted=1)
        context = {
            "title": "CodeRank - Tutorials",
            "tutorialsubtopictitle": tutorialsubtopictitle,
            "maintopicslug": maintopic,
            'subtopicslug': subtopic,
            "tutorialsubslug": tutorialsubtopic,
            "tutorialsubtopiccontent": tutorialsubtopiccontent,
            "form": form,
            "completedtutorialslist": tutorialsubtopiccompletedstatusquerylist,
            "pagetitle": "tutorial"
        }
        return redirect("TutorialSubTopicPage", maintopic=maintopic, subtopic=subtopic)

    return render(request, "tutorial_module/viewtutorial.html", context)
