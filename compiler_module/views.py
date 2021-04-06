from compete_module.models import CompeteModel, CompetitionOwnProblem
from login_module.models import Profile
from compiler_module.models import CompeteProblemResult, PracticeProblemResult
from django.contrib import messages
from compiler_module.forms import CodeForm
from django.http import request
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from practice_module.models import PracticeMainTopic, PracticeProblem, PracticeSubTopic, ProblemInfo
import requests
from time import sleep
from django.http.response import HttpResponse, JsonResponse
from django.contrib.auth.models import User


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
        dificulty = problemqueryset[0]['difficulty_id']
        score = problemqueryset[0]['score']
        attempted = probleminfoqueryset[0]['attempted']
        accuracy = probleminfoqueryset[0]['accuracy']
        tags = probleminfoqueryset[0]['tags']
        problem_content = list(
            PracticeProblem.objects.filter(slug=problem).values())
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
            "tags": tags,
            "difficulty": dificulty,
            "score": score
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
        problem_id = context["problemcontent"][0]["id"]
        submissionqueryset = PracticeProblemResult.objects.filter(problem_id = problem_id)
        context["pagetitle"] = "Submission"
        context["problemresults"] = submissionqueryset


    return render(request, "compiler_module/submission.html", context)


def SubmissionDetails(request, maintopic, subtopic, problemresult):
    if request.method == 'GET':
        problemresultqueryset = PracticeProblemResult.objects.filter(slug = problemresult)
        problemslug = problemresultqueryset[0].problem.slug
        context = {
            "resultdetails" :problemresultqueryset,
            "maintopic":maintopic,
            "subtopic":subtopic,
            "problem" :problemslug,
            "pagetitle":"Submission"
        }
    return render(request, "compiler_module/viewsubmission.html", context)


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


@login_required()
def Compile(request, maintopic, subtopic, problem):
    form = CodeForm()
    if request.is_ajax():
        code = request.POST['code']

        problem_content = list(
            PracticeProblem.objects.filter(slug=problem).values())

        testcases = [problem_content[0]["problemtestcaseoneinput"],
                     problem_content[0]["problemtestcasetwoinput"],
                     problem_content[0]["problemtestcasethreeinput"]]

        responselist = []
        for testcase in testcases:
            response = requests.post("https://api.jdoodle.com/v1/execute/", json={
                "clientId": "c33765ae70280c28efc025dba0ff7feb",
                "clientSecret": "d93477fefdb0b8bb94e7a063d0798b94d087b602e0114de048b16e169566ddde",
                "script": code,
                "stdin": testcase,
                "language": "python3",
                "versionIndex": "3"
            })
            parsed_json = response.json()
            print(parsed_json)
            responselist.append(parsed_json)
        return JsonResponse(responselist, safe=False)


@login_required()
def SubmitCode(request, maintopic, subtopic, problem):
    if request.is_ajax():
        code = request.POST['code']
        actualoutput1 = request.POST['actualoutput1']
        actualoutput2 = request.POST['actualoutput2']
        actualoutput3 = request.POST['actualoutput3']
        
        problem_content = list(
            PracticeProblem.objects.filter(slug=problem).values())

        testcases = [problem_content[0]["problemtestcaseoneoutput"],
                     problem_content[0]["problemtestcasetwooutput"],
                     problem_content[0]["problemtestcasethreeoutput"]]

        problemid = problem_content[0]["id"]

        userscore = 0
        testcasespassed = False
        useroutputonestatusid = 2
        useroutputtwostatusid = 2
        useroutputthreestatusid = 2

        cumulativeuserscorelist = list(Profile.objects.filter(
            user_id=request.user.id).values_list("score", flat=True))

        cumulativeuserscore = cumulativeuserscorelist[0]
        if actualoutput1.rstrip() == testcases[0] or actualoutput2.rstrip() == testcases[1] or actualoutput3.rstrip() == testcases[2]:
            score = problem_content[0]["score"]
            if actualoutput1.rstrip() == testcases[0] and actualoutput2.rstrip() == testcases[1] and actualoutput3.rstrip() == testcases[2]:
                userscore = score
                useroutputonestatusid, useroutputtwostatusid, useroutputthreestatusid = 1, 1, 1
                testcasespassed = True
            elif actualoutput1.rstrip() == testcases[0] and (actualoutput2.rstrip() == testcases[1] or actualoutput3.rstrip() == testcases[2]):
                userscore = score-(score/3)
                testcasespassed = True
                if actualoutput1.rstrip() == testcases[0]:
                    useroutputonestatusid = 1
                if actualoutput2.rstrip() == testcases[1]:
                    useroutputtwostatusid = 1
                if actualoutput3.rstrip() == testcases[2]:
                    useroutputthreestatusid = 1
            elif actualoutput1.rstrip() == testcases[0] or actualoutput2.rstrip() == testcases[1] or actualoutput3.rstrip() == testcases[2]:
                userscore = score-(score/3)-(score/3)
                testcasespassed = True
                if actualoutput1.rstrip() == testcases[0]:
                    useroutputonestatusid = 1
                if actualoutput2.rstrip() == testcases[1]:
                    useroutputtwostatusid = 1
                if actualoutput3.rstrip() == testcases[2]:
                    useroutputthreestatusid = 1
        else:
            testcasespassed = False
            useroutputonestatusid = 2
            useroutputtwostatusid = 2
            useroutputthreestatusid = 2
            return JsonResponse("NoTestCasesPassed", safe=False)

        issubmitted = False
        if testcasespassed:
            PracticeProblemResult.objects.create(
                useroutputone=actualoutput1,
                useroutputtwo=actualoutput2,
                useroutputthree=actualoutput3,
                score=userscore,
                code=code,
                problem_id=problem_content[0]["id"],
                user_id=request.user.id,
                useroutputonestatus_id=useroutputonestatusid,
                useroutputtwostatus_id=useroutputtwostatusid,
                useroutputthreestatus_id=useroutputthreestatusid
            )
            cumulativeuserscore += userscore
            problem_content = Profile.objects.filter(
                user_id=request.user.id).update(score=cumulativeuserscore)
            issubmitted = True
        else:
            return JsonResponse("NoTestCasesPassed", safe=False)
        if issubmitted:
            return JsonResponse("SubmittedSuccessfully", safe=False)
        else:
            return JsonResponse("ErrorSubmitting", safe=False)


@login_required
def TestCompiler(request, problem):
    if request.method == 'GET':
        form = CodeForm()
        testproblemqueryset = CompetitionOwnProblem.objects.filter(
            slug=problem)
        competitionid = list(CompetitionOwnProblem.objects.filter(
            slug=problem).values_list("competition_id", flat=True))
        competitonqueryset = CompeteModel.objects.filter(id=competitionid[0])
        context = {
            "problemcontent": testproblemqueryset,
            "form": form,
            "problem": problem,
            "competitiondetails": competitonqueryset
        }
    return render(request, "compiler_module/testcompiler.html", context)


@login_required()
def TestCompile(request, problem):
    form = CodeForm()
    if request.is_ajax():
        code = request.POST['code']

        problem_content = list(
            CompetitionOwnProblem.objects.filter(slug=problem).values())

        testcases = [problem_content[0]["problemtestcaseoneinput"],
                     problem_content[0]["problemtestcasetwoinput"],
                     problem_content[0]["problemtestcasethreeinput"]]

        responselist = []
        for testcase in testcases:
            response = requests.post("https://api.jdoodle.com/v1/execute/", json={
                "clientId": "c33765ae70280c28efc025dba0ff7feb",
                "clientSecret": "d93477fefdb0b8bb94e7a063d0798b94d087b602e0114de048b16e169566ddde",
                "script": code,
                "stdin": testcase,
                "language": "python3",
                "versionIndex": "3"
            })
            parsed_json = response.json()
            print(parsed_json)
            responselist.append(parsed_json)
        return JsonResponse(responselist, safe=False)


@login_required()
def TestSubmitCode(request, problem):
    if request.is_ajax():
        code = request.POST['code']
        actualoutput1 = request.POST['actualoutput1']
        actualoutput2 = request.POST['actualoutput2']
        actualoutput3 = request.POST['actualoutput3']

        problem_content = list(
            CompetitionOwnProblem.objects.filter(slug=problem).values())

        testcases = [problem_content[0]["problemtestcaseoneoutput"],
                     problem_content[0]["problemtestcasetwooutput"],
                     problem_content[0]["problemtestcasethreeoutput"]]

        userscore = 0
        testcasespassed = False
        useroutputonestatusid = 2
        useroutputtwostatusid = 2
        useroutputthreestatusid = 2
        issubmitted = False

        if actualoutput1.rstrip() == testcases[0] or actualoutput2.rstrip() == testcases[1] or actualoutput3.rstrip() == testcases[2]:
            score = problem_content[0]["score"]
            if actualoutput1.rstrip() == testcases[0] and actualoutput2.rstrip() == testcases[1] and actualoutput3.rstrip() == testcases[2]:
                userscore = score
                useroutputonestatusid, useroutputtwostatusid, useroutputthreestatusid = 1, 1, 1
                testcasespassed = True
            elif actualoutput1.rstrip() == testcases[0] and (actualoutput2.rstrip() == testcases[1] or actualoutput3.rstrip() == testcases[2]):
                userscore = score-(score/3)
                testcasespassed = True
                if actualoutput1.rstrip() == testcases[0]:
                    useroutputonestatusid = 1
                if actualoutput2.rstrip() == testcases[1]:
                    useroutputtwostatusid = 1
                if actualoutput3.rstrip() == testcases[2]:
                    useroutputthreestatusid = 1
            elif actualoutput1.rstrip() == testcases[0] or actualoutput2.rstrip() == testcases[1] or actualoutput3.rstrip() == testcases[2]:
                userscore = score-(score/3)-(score/3)
                testcasespassed = True
                if actualoutput1.rstrip() == testcases[0]:
                    useroutputonestatusid = 1
                if actualoutput2.rstrip() == testcases[1]:
                    useroutputtwostatusid = 1
                if actualoutput3.rstrip() == testcases[2]:
                    useroutputthreestatusid = 1
        else:
            testcasespassed = False
            useroutputonestatusid = 2
            useroutputtwostatusid = 2
            useroutputthreestatusid = 2
            return JsonResponse("NoTestCasesPassed", safe=False)

        if testcasespassed:
            CompeteProblemResult.objects.create(
                useroutputone=actualoutput1,
                useroutputtwo=actualoutput2,
                useroutputthree=actualoutput3,
                score=userscore,
                code=code,
                problem_id=problem_content[0]["id"],
                competition_id=problem_content[0]["competition_id"],
                user_id=request.user.id,
                useroutputonestatus_id=useroutputonestatusid,
                useroutputtwostatus_id=useroutputtwostatusid,
                useroutputthreestatus_id=useroutputthreestatusid
            )
            issubmitted = True
        else:
            return JsonResponse("NoTestCasesPassed", safe=False)
        if issubmitted:
            return JsonResponse("SubmittedSuccessfully", safe=False)
        else:
            return JsonResponse("ErrorSubmitting", safe=False)
