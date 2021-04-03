from practice_module.models import PracticeProblem
from compete_module.models import CompeteModel, CompetitionOwnProblem, CompetitionType, RegisteredUserCompete, Status
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib import messages


# Create your views here.


@login_required
def UpcomingPage(request):
    if request.method == "GET":
        opencompetitionsdetailsqueryset = CompeteModel.objects.filter(
            status_id=1)
        registeredcompetitionsquerylist = list(
            RegisteredUserCompete.objects.all().values())
        userid = request.user.id
        registeredcompetitionids = []
        for registeredcompetitions in registeredcompetitionsquerylist:
            if userid == registeredcompetitions['user_id']:
                registeredcompetitionids.append(
                    registeredcompetitions['competition_id'])

        context = {
            "title": "CodeRank - Upcoming Competitions",
            "opencompetitions": opencompetitionsdetailsqueryset,
            "registeredcompetitions": registeredcompetitionids,
            "pagetitle": "upcomingpage"
        }
    return render(request, "compete_module/upcoming.html", context)


@login_required
def OngoingPage(request):
    if request.method == "GET":
        ongoingcompetitions = CompeteModel.objects.filter(status_id=2)
        context = {
            "title": "CodeRank - Ongoing competitions",
            "ongoingcompetitions": ongoingcompetitions,
            "pagetitle": "ongoingpage"
        }
    return render(request, "compete_module/ongoing.html", context)


@login_required
def PreviousPage(request):
    if request.method == "GET":
        previouscompetitions = CompeteModel.objects.filter(status_id=3)
        context = {
            "title": "CodeRank - Previous Competitions",
            "previouscompetitions": previouscompetitions,
            "pagetitle": "previouspage"
        }
    return render(request, "compete_module/previous.html", context)


@login_required
def RigsteredPage(request):
    if request.method == "GET":
        userid = request.user.id
        registeredcompetitionquerylist = list(RegisteredUserCompete.objects.filter(
            user_id=userid).values())
        registeredcompetition = []
        for competion in registeredcompetitionquerylist:
            temp = CompeteModel.objects.filter(
                id=competion["competition_id"])
            registeredcompetition.append(temp)
        context = {
            "title": "CodeRank - Regitsered Competitions",
            "registeredcompetitions": registeredcompetition,
            "pagetitle": "registeredpage"
        }
    return render(request, "compete_module/registered.html", context)


@ login_required
def ViewCompetitionDetails(request, competitionslug):
    competitiondetailsquerylist = list(CompeteModel.objects.filter(
        slug=competitionslug).values())
    competitiondetails = CompeteModel.objects.filter(
        slug=competitionslug)
    competitiontitle = competitiondetailsquerylist[0]['competitiontitle']
    competitiontypeid = competitiondetailsquerylist[0]['type_id']
    competitiontypequerylist = list(CompetitionType.objects.filter(
        id=competitiontypeid).values())
    competitiontype = competitiontypequerylist[0]['type']
    competitionid = competitiondetailsquerylist[0]['id']
    registereduserquerylist = list(
        RegisteredUserCompete.objects.filter(competition_id=competitionid).values())
    userid = request.user.id
    status = None
    try:
        status = competitiondetailsquerylist[0]["status_id"]
    except:
        status = 0
    if request.method == "GET":
        if len(registereduserquerylist) > 0 and registereduserquerylist[0]['user_id'] == userid:
            context = {
                "title": "CodeRank - Compete",
                "competitiondetails": competitiondetails,
                "pagetitle": "registeredpage",
                "competitiontitle": competitiontitle,
                "competitiontype": competitiontype,
                "isregistered": True
            }
        else:
            context = {
                "title": "CodeRank - Compete",
                "competitiondetails": competitiondetails,
                "pagetitle": "registeredpage",
                "competitiontitle": competitiontitle,
                "competitiontype": competitiontype,
            }

    elif request.method == "POST":
        if len(registereduserquerylist) > 0 and registereduserquerylist[0]['user_id'] == userid:
            context = {
                "competitiondetails": competitiondetails,
                "pagetitle": "registeredpage",
                "competitiontitle": competitiontitle,
                "competitiontype": competitiontype,
                "isregistered": True
            }
        else:
            RegisteredUserCompete.objects.create(
                user_id=userid, competition_id=competitionid, registeredon=timezone.now())
            context = {
                "competitiondetails": competitiondetails,
                "pagetitle": "registeredpage",
                "competitiontitle": competitiontitle,
                "competitiontype": competitiontype,
            }
            if status == 2:
                messages.success(
                    request, f"Successfully registered to the event {competitiontitle} now you can continue with the assessment. All the best!")
                return redirect("AssessmentStartPage", competitionslug=competitionslug)
            else:
                messages.success(
                    request, f"Successfully registered to the event {competitiontitle}")
                return redirect("CompeteUpcoming")

    return render(request, "compete_module/viewdetails.html", context)


def AssessmentStartPage(request, competitionslug):
    competitionidlist = list(CompeteModel.objects.filter(
        slug=competitionslug).values_list("id", flat=True))
    competitionid = competitionidlist[0]
    registreduseridlist = list(RegisteredUserCompete.objects.filter(
        competition_id=competitionid).values_list("user_id", flat=True))

    if len(registreduseridlist) == 0:
        messages.warning(
            request, f"You must register the event first then continue to take assessment!")
        return redirect("RegisterCompetition", competitionslug=competitionslug)
    else:
        competitiondetailsqueryset = CompeteModel.objects.filter(
            slug=competitionslug)
        context = {
            "title": "CodeRank - Assessment",
            "competitiondetails": competitiondetailsqueryset
        }
    return render(request, "compete_module/taketest.html", context)


def AssessmentListPage(request, competitionslug):
    competitionid = list(CompeteModel.objects.filter(
        slug=competitionslug).values_list("id", flat=True))[0]
    problems = CompetitionOwnProblem.objects.filter(
        competition_id=competitionid)

    # solvedproblemid = []
    # solvedproblemquerylist = list(PracticeProblemResult.objects.filter(
    #     user_id=request.user.id).values())

    # for solvedproblem in solvedproblemquerylist:
    #     solvedproblemid.append(solvedproblem["problem_id"])

    context = {
        "problems": problems,
    }

    return render(request, "compete_module/testproblemlist.html", context)
