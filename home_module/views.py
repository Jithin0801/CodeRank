from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def DevHomePage(request):
    return render(request, "home_module/home.html", {"title": "CodeRank - Home"})
