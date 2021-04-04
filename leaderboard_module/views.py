from login_module.models import Profile
from django.shortcuts import render

# Create your views here.


def LeaderBoard(request):
    if request.method == "GET":
        profilequeryset = Profile.objects.all().order_by("-score")

        context = {
            "title": "CodeRank - Leaderboard",
            "profilelist": profilequeryset
        }
    return render(request, "leaderboard_module/leaderboard.html", context)
