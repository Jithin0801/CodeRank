from compiler_module.forms import CodeForm
from django.http import request
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from practice_module.models import PracticeMainTopic, PracticeProblem, PracticeSubTopic, ProblemInfo

class ProblemDetailsSet():
    def getDetails(self, request, maintopic, subtopic, problem):
        maintopicquertset = list(
            PracticeMainTopic.objects.filter(slug=maintopic).values())
        subtopicqueryset = list(
            PracticeSubTopic.objects.filter(slug=subtopic).values())
        problemqueryset = list(
            PracticeProblem.objects.filter(slug=problem).values())
        probleminfoqueryset = list(
            ProblemInfo.objects.filter(problem_id=problemqueryset[0]['id']).values())
        maintitle = maintopicquertset[0]['title']
        subtitle = subtopicqueryset[0]['title']
        problemtitle = problemqueryset[0]['problemtitle']
        attempted = probleminfoqueryset[0]['attempted']
        accuracy = probleminfoqueryset[0]['accuracy']
        tags = probleminfoqueryset[0]['tags']
        problem_content = PracticeProblem.objects.filter(slug=problem)
        context = {
            "title": "CodeRank - Solve",
            "problemcontent": problem_content,
            "problem": problem,
            "maintitle": maintitle,
            "maintopic": maintopic,
            "subtitle": subtitle,
            "subtopic": subtopic,
            "problemtitle": problemtitle,
            "attempted": attempted,
            "accuracy": accuracy,
            "tags": tags
        }
        return context


@login_required
def Compiler(request, maintopic, subtopic, problem):
    if request.method == 'GET':
        form = CodeForm()
        problemset = ProblemDetailsSet()
        context = problemset.getDetails(request, maintopic, subtopic, problem)
        context["pagetitle"] = "Compiler"
        context["form"] = form
    return render(request, "compiler_module/compiler.html", context)


@login_required
def Submission(request, maintopic, subtopic, problem):
    if request.method == 'GET':
        problemset = ProblemDetailsSet()
        context = problemset.getDetails(request, maintopic, subtopic, problem)
        context["pagetitle"] = "Submission"
    return render(request, "compiler_module/submission.html", context)


@login_required
def Discussion(request, maintopic, subtopic, problem):
    if request.method == 'GET':
        problemset = ProblemDetailsSet()
        context = problemset.getDetails(request, maintopic, subtopic, problem)
        context["pagetitle"] = "Discussion"
    return render(request, "compiler_module/discussion.html", context)


@login_required
def LeaderBoard(request, maintopic, subtopic, problem):
    if request.method == 'GET':
        problemset = ProblemDetailsSet()
        context = problemset.getDetails(request, maintopic, subtopic, problem)
        context["pagetitle"] = "Leaderboard"
    return render(request, "compiler_module/leaderboard.html", context)
