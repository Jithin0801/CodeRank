from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def DevHomePage(request):
    return render(request, "home_module/base.html", {"title": "CodeRank - Home"})
