from compiler_module.models import PracticeProblemResult
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import PracticeMainTopic, PracticeProblem, PracticeSubTopic
# Create your views here.


@login_required
def PracticePage(request):
    if request.method == 'GET':
        main_topic = PracticeMainTopic.objects.all()
        sub_topic = PracticeSubTopic.objects.all()
        context = {
            "title": "CodeRank - Practice",
            "main": main_topic,
            "sub": sub_topic,
            "pagetitle":"practice"
        }
    return render(request, "practice_module/practice.html", context)


@login_required
def ViewChallenges(request, maintopic, subtopic):
    if request.method == 'GET':
        topicid = PracticeSubTopic.objects.filter(
            slug=subtopic).values_list('id', flat=True)
        maintopicquertset = list(
            PracticeMainTopic.objects.filter(slug=maintopic).values())
        subtopicqueryset = list(
            PracticeSubTopic.objects.filter(slug=subtopic).values())
        maintitle = maintopicquertset[0]['title']
        subtitle = subtopicqueryset[0]['title']
        problems = PracticeProblem.objects.filter(subtopic_id=topicid[0])

        solvedproblemid = []
        solvedproblemquerylist = list(PracticeProblemResult.objects.filter(
            user_id=request.user.id).values())

        for solvedproblem in solvedproblemquerylist:
            solvedproblemid.append(solvedproblem["problem_id"])

        context = {
            "title": "CodeRank - Practice",
            "problems": problems,
            "maintitle": maintitle,
            "subtitle": subtitle,
            "maintopic": maintopic,
            "subtopic": subtopic,
            "solvedproblems": solvedproblemid,
            "pagetitle": "practice"
        }
    return render(request, "practice_module/viewchallenges.html", context)
