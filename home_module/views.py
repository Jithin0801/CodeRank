from home_module.models import AlgorithmTopic, DSTopic
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def DevHomePage(request):
    return render(request, "home_module/base.html", {"title": "CodeRank - Home"})


def PracticePage(request):
    if request.method == 'GET':
        data_sturcture_topics = DSTopic.objects.all()
        algorithm_topics = AlgorithmTopic.objects.all()
        context = {
            "title":"CodeRank - Practice",
            "ds":data_sturcture_topics,
            "algo":algorithm_topics
        }
    return render(request, "home_module/practice.html", context)
