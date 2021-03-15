from django.shortcuts import render
from .models import PracticeMainTopic, PracticeSubTopic
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
        print(PracticeSubTopic.objects.filter(maintopic=1))
    return render(request, "practice_module/practice.html", context)
