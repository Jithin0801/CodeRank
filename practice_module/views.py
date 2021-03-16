from django.shortcuts import render
from .models import PracticeMainTopic, PracticeProblem, PracticeSubTopic
# Create your views here.


def PracticePage(request):
    if request.method == 'GET':
        main_topic = PracticeMainTopic.objects.all()
        sub_topic = PracticeSubTopic.objects.all()
        context = {
            "title": "CodeRank - Practice",
            "main": main_topic,
            "sub": sub_topic
        }
    return render(request, "practice_module/practice.html", context)

def ViewChallenges(request, maintopic, subtopic):
    if request.method == 'GET':
        topicid = PracticeSubTopic.objects.filter(slug = subtopic).values_list('id', flat=True)
        maintopicquertset = list(PracticeMainTopic.objects.filter(slug = maintopic).values())
        subtopicqueryset = list(PracticeSubTopic.objects.filter(slug = subtopic).values())
        maintitle = maintopicquertset[0]['title']
        subtitle = subtopicqueryset[0]['title']

        problems = PracticeProblem.objects.filter(topic_id = topicid[0])
        context = {
            "title": "CodeRank - Practice",
            "problems": problems,
            "maintopic": maintitle,
            "subtopic": subtitle
        }
    return render(request, "practice_module/viewchallenges.html", context)
