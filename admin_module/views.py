from blog_module.forms import PostBlogForm
from compiler_module.models import CompeteProblemResult
from login_module.models import Profile
from blog_module.models import BlogModel
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify
from admin_module.models import InstitutionProfile
from admin_module.forms import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.admin.views.decorators import staff_member_required
from practice_module.models import PracticeMainTopic, PracticeSubTopic, PracticeProblem
from tutorial_module.models import TutorialContent, TutorialSubtopic
from compete_module.models import CompeteModel, CompetitionOwnProblem, CompetitionResult, RegisteredUserCompete
from django.utils import timezone
# Create your views here.


def InsitiutionHomePage(request):
    return render(request, "admin_module/home.html")


def InstitutionSignUpPage(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            formdata = form.cleaned_data
            try:
                user = User.objects.create(
                    username=formdata['username'], first_name=formdata['first_name'], last_name=formdata['last_name'],
                    email=formdata['email'], is_staff=True)
                user.set_password(formdata['password2'])
                user.save()
                username = form.cleaned_data.get('username')
            except:
                messages.success(request, f'Error creating account')
                return redirect("InstitutionSignUpPage")
            messages.success(
                request, f'Account created for { username }, Now login!')
            return redirect("InstitutionLoginPage")
        else:
            pass
    else:
        form = UserRegistrationForm()
    return render(request, "admin_module/inssignup.html", {"title": "CodeRank - Sign Up", "form": form, "pagetitle": "signup"})


def InstitutionLoginPage(request):
    if request.method == "POST":
        form = AuthenticationForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_staff:
                form = login(request, user)
                try:
                    user.institutionprofile
                except:
                    return redirect('InsCompleteProfile')
                else:
                    return redirect('MainTopicList')
            else:
                messages.error(
                    request, f'You are not a staff member')
        else:
            messages.error(
                request, "Username or Password is incorrect")

    form = AuthenticationForm()
    return render(request, "admin_module/inslogin.html", {"title": "CodeRank - Log In", "form": form, "pagetitle": "login"})


@staff_member_required
@login_required
def InsCompleteProfile(request):
    if request.method == 'POST':
        profile = InstitutionProfile.objects.create(user=request.user)
        UserUpdationform = UserUpdationForm(
            request.POST, instance=request.user)
        ProfileUpdationform = InsProfileUpdationForm(
            request.POST, request.FILES, instance=request.user.institutionprofile)
        if UserUpdationform.is_valid() and ProfileUpdationform.is_valid():
            UserUpdationform.save()
            ProfileUpdationform.save()
            messages.success(request, "Your information has been updated!")
            return redirect('MainTopicList')
    else:
        ProfileUpdationform = InsProfileUpdationForm()
        UserUpdationform = UserUpdationForm(instance=request.user)
    return render(request, "admin_module/inscompleteprofile.html", {"title": "Welcome-Complete your profile", "ProfileUpdationform": ProfileUpdationform, "UserUpdationForm": UserUpdationform})


@staff_member_required
@login_required
def InsDashboard(request):
    context = {
        "title": "CodeRank - Dashboard",
        "pagetitle": "dash"
    }
    return render(request, "admin_module/dashboard.html", context)


@staff_member_required
@login_required
def MainTopicList(request):
    maintopicqueryset = PracticeMainTopic.objects.all()
    context = {
        "title": "CodeRank - Main Topic",
        "maintopiclist": maintopicqueryset,
        "pagetitle": "main"
    }
    return render(request, "admin_module/maintopiclist.html", context)


@staff_member_required
@login_required
def AddNewMainTopic(request):
    form = AddNewMainTopicForm()
    if request.method == 'GET':
        context = {
            "title": "CodeRank - Add new topic",
            "pagetitle": "prob",
            "form": form
        }
    elif request.method == 'POST':
        form = AddNewMainTopicForm(request.POST)
        if form.is_valid():
            form.save()
            title = form.cleaned_data.get('title')
            messages.success(
                request, f"{title} has been added successfully!")
            return redirect('MainTopicList')

    return render(request, "admin_module/addnewtopic.html", context)


@staff_member_required
@login_required
def UpdateMainTopic(request, maintopic):
    maintopictitlelist = list(PracticeMainTopic.objects.filter(
        slug=maintopic).values_list('title', flat=True))
    form_data = {
        "title": maintopictitlelist[0],
    }
    form = UpdateMainTopicForm(initial=form_data)
    if request.method == 'GET':
        context = {
            "title": "CodeRank - Update topic",
            "pagetitle": "prob",
            "form": form
        }
    elif request.method == 'POST':
        form = AddNewMainTopicForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            PracticeMainTopic.objects.filer(slug=maintopic).update(title=title)
            messages.success(
                request, f"{title} has been updated successfully!")
            return redirect('MainTopicList')

    return render(request, "admin_module/edittopic.html", context)


@staff_member_required
@login_required
def DelMainTopic(request, maintopic):
    maintopictquerylist = list(PracticeMainTopic.objects.filter(
        slug=maintopic).values())
    maintopictitle = maintopictquerylist[0]['title']
    form = DelMainTopicForm()
    if request.method == 'GET':
        context = {
            "title": "CodeRank - Update topic",
            "pagetitle": "main",
            "maintopictitle": maintopictquerylist[0]['title'],
            "form": form,
            "maintopicslug": maintopic,
        }
    elif request.method == 'POST':
        form = DelMainTopicForm(request.POST)
        PracticeMainTopic.objects.filter(slug=maintopic).delete()
        messages.success(
            request, f"{maintopictitle} has been deleted successfully!")
        return redirect('MainTopicList')
    return render(request, "admin_module/deletemaintopic.html", context)


@staff_member_required
@login_required
def SubTopicList(request, maintopic):
    maintopicid = list(PracticeMainTopic.objects.filter(
        slug=maintopic).values_list("id", flat=True))
    maintopictitle = list(PracticeMainTopic.objects.filter(
        slug=maintopic).values_list("title", flat=True))
    subtopicqueryset = PracticeSubTopic.objects.filter(
        maintopic_id=maintopicid[0])
    context = {
        "title": "CodeRank - Sub Topic",
        "subtopiclist": subtopicqueryset,
        "maintopicslug": maintopic,
        "maintopictitle": maintopictitle[0],
        "pagetitle": "main"
    }
    return render(request, "admin_module/subtopiclist.html", context)


@staff_member_required
@login_required
def AddNewSubTopic(request, maintopic):
    maintopicid = list(PracticeMainTopic.objects.filter(
        slug=maintopic).values_list("id", flat=True))
    form = AddNewSubTopicForm()
    if request.method == 'GET':
        context = {
            "title": "CodeRank - Add new topic",
            "pagetitle": "main",
            "form": form
        }
    elif request.method == 'POST':
        form = AddNewSubTopicForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            PracticeSubTopic.objects.update_or_create(
                maintopic_id=maintopicid[0], title=data['title'], content=data['content'])
            messages.success(
                request, f"{data['title']} has been added successfully!")
            return redirect('SubTopicList', maintopic=maintopic)

    return render(request, "admin_module/addnewtopic.html", context)


@staff_member_required
@login_required
def ViewSubTopicContent(request, maintopic, subtopic):
    subtopicqueryset = PracticeSubTopic.objects.filter(slug=subtopic)
    subtopictitle = list(PracticeSubTopic.objects.filter(
        slug=subtopic).values_list('title', flat=True))
    context = {
        "title": "CodeRank - View topic",
        "pagetitle": "main",
        "subtopictitle": subtopictitle[0],
        "subtopicqueryset": subtopicqueryset,
        "maintopicslug": maintopic,
        "subtopicslug": subtopic
    }
    return render(request, 'admin_module/viewtopic.html', context)


@staff_member_required
@login_required
def UpdateSubTopic(request, maintopic, subtopic):
    subtopictquerylist = list(PracticeSubTopic.objects.filter(
        slug=subtopic).values())
    form_data = {
        "title": subtopictquerylist[0]['title'],
        "content": subtopictquerylist[0]['content']
    }
    form = UpdateSubTopicForm(initial=form_data)
    if request.method == 'GET':
        context = {
            "title": "CodeRank - Update topic",
            "pagetitle": "main",
            "subtopictitle": subtopictquerylist[0]['title'],
            "form": form
        }
    elif request.method == 'POST':
        form = UpdateSubTopicForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            content = form.cleaned_data.get('content')
            PracticeSubTopic.objects.filter(slug=subtopic).update(
                title=title, content=content)
            messages.success(
                request, f"{title} has been updated successfully!")
            return redirect('ViewSubTopicContent', maintopic=maintopic, subtopic=subtopic)

    return render(request, "admin_module/edittopic.html", context)


@staff_member_required
@login_required
def DelSubTopic(request, maintopic, subtopic):
    subtopictquerylist = list(PracticeSubTopic.objects.filter(
        slug=subtopic).values())
    title = subtopictquerylist[0]['title']
    form = DelSubTopicForm()
    if request.method == 'GET':
        context = {
            "title": "CodeRank - Update topic",
            "pagetitle": "main",
            "subtopictitle": subtopictquerylist[0]['title'],
            "form": form,
            "maintopicslug": maintopic,
            "subtopicslug": subtopic
        }
    elif request.method == 'POST':
        form = DelSubTopicForm(request.POST)
        PracticeSubTopic.objects.filter(slug=subtopic).delete()
        messages.success(
            request, f"{title} has been deleted successfully!")
        return redirect('SubTopicList', maintopic=maintopic)
    return render(request, "admin_module/deletesubtopic.html", context)


@staff_member_required
@login_required
def InsTutorialsList(request):
    tutorialsubtopicqueryset = TutorialSubtopic.objects.all()
    context = {
        "title": "CodeRank - Tutorials",
        "tutorials": tutorialsubtopicqueryset,
        "pagetitle": "tuto"
    }
    return render(request, "admin_module/tutorialslist.html", context)


@staff_member_required
@login_required
def InsViewTutorial(request, tutorialsubtopic):
    tutorialsubtopicidlist = list(TutorialSubtopic.objects.filter(
        slug=tutorialsubtopic).values_list("id", flat=True))
    tutorialsubtopiclist = list(TutorialSubtopic.objects.filter(
        slug=tutorialsubtopic).values())
    tutorialcontentqueryset = TutorialContent.objects.filter(
        tutorialsubtopic_id=tutorialsubtopicidlist[0])
    context = {
        "title": "CodeRank - Tutorials",
        "tutorials": tutorialcontentqueryset,
        "title": tutorialsubtopiclist[0]['title'],
        "tutorialsubtopicslug": tutorialsubtopic,
        "pagetitle": "tuto"
    }
    return render(request, "admin_module/viewtutorial.html", context)


@staff_member_required
@login_required
def InsDelTutorial(request, tutorialsubtopic):
    tutorialsubtopictquerylist = list(TutorialSubtopic.objects.filter(
        slug=tutorialsubtopic).values())
    title = tutorialsubtopictquerylist[0]['title']
    form = DelTutorialSubTopic()
    if request.method == 'GET':
        context = {
            "title": "CodeRank - Update topic",
            "pagetitle": "main",
            "title": tutorialsubtopictquerylist[0]['title'],
            "form": form,
            "tutorialsubtopicslug": tutorialsubtopic
        }
    elif request.method == 'POST':
        form = DelSubTopicForm(request.POST)
        TutorialSubtopic.objects.filter(slug=tutorialsubtopic).delete()
        messages.success(
            request, f"\"{title}\" has been deleted successfully!")
        return redirect('InsTutorialsList')
    return render(request, "admin_module/deletetutorial.html", context)


@staff_member_required
@login_required
def InsEditTutorial(request, tutorialsubtopic):
    tutorialsubtopictquerylist = list(TutorialSubtopic.objects.filter(
        slug=tutorialsubtopic).values())
    title = tutorialsubtopictquerylist[0]['title']
    tutorialsubtopicidid = tutorialsubtopictquerylist[0]['id']
    tutorialcontentquerylist = list(TutorialContent.objects.filter(
        tutorialsubtopic_id=tutorialsubtopicidid).values())
    title_form_data = {
        "subtopic": tutorialsubtopictquerylist[0]['subtopic_id'],
        "title": title
    }
    content_form_data = {
        "content": tutorialcontentquerylist[0]['content'],
        "exampleone": tutorialcontentquerylist[0]['exampleone'],
        "exampletwo": tutorialcontentquerylist[0]['exampletwo']
    }

    titleform = EditTutorialSubTopic(initial=title_form_data)
    contentfrom = EditTutorialContent(initial=content_form_data)

    context = {
        "titleform": titleform,
        "contentfrom": contentfrom,
        "title": title,
        "tutorialsubtopicslug": tutorialsubtopic
    }

    if request.method == "POST":
        titleform = EditTutorialSubTopic(request.POST)
        contentfrom = EditTutorialContent(request.POST)

        if titleform.is_valid() and contentfrom.is_valid():
            TutorialSubtopic.objects.filter(slug=tutorialsubtopic).update(
                subtopic_id=tutorialsubtopictquerylist[0]['subtopic_id'], title=titleform.cleaned_data.get("title"))
            TutorialContent.objects.filter(tutorialsubtopic_id=tutorialcontentquerylist[0]['tutorialsubtopic_id']).update(
                content=contentfrom.cleaned_data.get("content"), exampleone=contentfrom.cleaned_data.get("exampleone"),
                exampletwo=contentfrom.cleaned_data.get("exampletwo"))
            newtitle = titleform.cleaned_data.get('title')
            messages.success(
                request, f"\"{newtitle}\" has been updated successfully!")
        return redirect('InsViewTutorial', tutorialsubtopic=tutorialsubtopic)
    return render(request, 'admin_module/edittutorial.html', context)


@staff_member_required
@login_required
def InsAddTutorial(request):
    titleform = AddTutorialSubTopicForm()
    contentfrom = AddTutorialContentForm()
    context = {
        "titleform": titleform,
        "contentfrom": contentfrom,
    }
    if request.method == "POST":
        titleform = AddTutorialSubTopicForm(request.POST)
        contentfrom = AddTutorialContentForm(request.POST)
        if titleform.is_valid() and contentfrom.is_valid():
            titleformdata = titleform.cleaned_data
            TutorialSubtopic.objects.create(
                title=titleformdata['title'], subtopic_id=titleformdata['subtopic_id'].id)
            titleslug = slugify(titleformdata['title'])
            tutorialsubtopicid = list(TutorialSubtopic.objects.filter(
                slug=titleslug).values_list("id", flat=True))[0]
            contentformdata = contentfrom.cleaned_data
            TutorialContent.objects.create(content=contentformdata['content'],
                                           exampleone=contentformdata['exampleone'],
                                           exampletwo=contentformdata['exampletwo'], tutorialsubtopic_id=tutorialsubtopicid)
            messages.success(
                request, f"\"\" has been added successfully!")
        return redirect('InsTutorialsList')
    return render(request, 'admin_module/addtutorial.html', context)


@ staff_member_required
@login_required
def InsCompetitionsList(request):
    competitionqueryset = CompeteModel.objects.filter(
        posted_by_id=request.user.id)
    context = {
        "competitions": competitionqueryset,
        "title": "CodeRank - Competitions",
        "pagetitle": "comp"
    }
    return render(request, "admin_module/competitionslist.html", context)


@ staff_member_required
@login_required
def InsAddCompetition(request):
    form = AddCompetitionForm()
    if request.method == 'GET':
        context = {
            "form": form,
            "title": "CodeRank - Competitions",
            "pagetitle": "comp"
        }
    elif request.method == 'POST':
        form = AddCompetitionForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            title = form_data['competition_title']
            CompeteModel.objects.create(competition_title=form_data['competition_title'],
                                        competition_description=form_data['competition_description'],
                                        registration_start_date=form_data['registration_start_date'],
                                        registration_end_date=form_data['registration_end_date'],
                                        competition_start_date=form_data['competition_start_date'],
                                        competition_end_date=form_data['competition_end_date'],
                                        assessment_time=form_data['assessment_time'],
                                        status_id=form_data['status_id'].id,
                                        type_id=form_data['type_id'].id,
                                        posted_by_id=request.user.id)
            messages.success(
                request, f"\"{title}\" has been added successfully!")
            return redirect('InsCompetitionsList')

    return render(request, "admin_module/addcompetition.html", context)


@staff_member_required
@login_required
def InsDelCompetition(request, competitiontitle):
    competitionquerylist = list(CompeteModel.objects.filter(
        slug=competitiontitle).values())
    title = competitionquerylist[0]['competition_title']
    form = DelCompetitionForm()
    if request.method == 'GET':
        context = {
            "title": "CodeRank - Delete Competition",
            "pagetitle": "main",
            "title": competitionquerylist[0]['competition_title'],
            "form": form,
            "competitiontitleslug": competitiontitle
        }
    elif request.method == 'POST':
        form = DelCompetitionForm(request.POST)
        CompeteModel.objects.filter(slug=competitiontitle).delete()
        messages.success(
            request, f"\"{title}\" has been deleted successfully!")
        return redirect('InsCompetitionsList')
    return render(request, "admin_module/deletecompetition.html", context)


@staff_member_required
@login_required
def InsEditCompetition(request, competitiontitle):
    competitionquerylist = list(CompeteModel.objects.filter(
        slug=competitiontitle).values())
    title = competitionquerylist[0]['competition_title']
    instance = get_object_or_404(CompeteModel, slug=competitiontitle)
    form = EditCompetitionForm(instance=instance)

    if request.method == 'GET':
        context = {
            "title": "CodeRank - Delete Competition",
            "pagetitle": "main",
            "title": competitionquerylist[0]['competition_title'],
            "form": form,
            "competitiontitleslug": competitiontitle
        }
    elif request.method == 'POST':
        form = EditCompetitionForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            title = form_data['competition_title']
            CompeteModel.objects.filter(slug=competitiontitle).update(competition_title=form_data['competition_title'],
                                                                      competition_description=form_data[
                                                                          'competition_description'],
                                                                      registration_start_date=form_data[
                                                                          'registration_start_date'],
                                                                      registration_end_date=form_data[
                                                                          'registration_end_date'],
                                                                      competition_start_date=form_data[
                                                                          'competition_start_date'],
                                                                      competition_end_date=form_data[
                                                                          'competition_end_date'],
                                                                      assessment_time=form_data['assessment_time'],
                                                                      status_id=form_data['status'].id,
                                                                      type_id=form_data['type'].id,
                                                                      posted_by_id=request.user.id)
            messages.success(
                request, f"\"{title}\" has been updated successfully!")
            return redirect('ViewCompetitionDetails', competitiontitle=competitiontitle)
    return render(request, "admin_module/editcompetition.html", context)


@staff_member_required
@login_required
def ResigteredUsers(request, competitiontitle):
    competitionquerylist = list(CompeteModel.objects.filter(
        slug=competitiontitle).values())
    title = competitionquerylist[0]['competition_title']
    competitionid = competitionquerylist[0]['id']
    profilelist = RegisteredUserCompete.objects.filter(
        competition_id=competitionid)
    context = {
        "title": "CodeRank - Users",
        "pagetitle": "comp",
        "title": title,
        "competitiontitleslug": competitiontitle,
        "profilelist": profilelist
    }
    return render(request, 'admin_module/reguserslist.html', context)


@staff_member_required
@login_required
def DelResigteredUser(request, competitiontitle, nameslug):
    competitionquerylist = list(CompeteModel.objects.filter(
        slug=competitiontitle).values())
    profilequerylist = list(Profile.objects.filter(
        slug=nameslug).values())
    competitionid = competitionquerylist[0]['id']
    title = competitionquerylist[0]['competition_title']
    userid = profilequerylist[0]['id']
    userquerylist = list(User.objects.filter(id=userid).values())
    username = userquerylist[0]['first_name'] + \
        " " + userquerylist[0]['last_name']
    context = {
        "pagetitle": "comp",
        "smalltitle": "Remove User",
        "maintitle": username,
        "exp": f"\"{username}\" will be unenrolled from the competition \"{title}\""
    }
    if request.method == 'POST':
        RegisteredUserCompete.objects.filter(
            competition_id=competitionid).filter(user_id=userid).delete()
        messages.success(
            request, f'\"{username}\" removed from the registered users list successfully!')
        return redirect("ResigteredUsers", competitiontitle=competitiontitle)

    return render(request, 'admin_module/deletecompetitioncontent.html', context)


@staff_member_required
@login_required
def ViewCompetitionDetails(request, competitiontitle):
    competitionqueryset = CompeteModel.objects.filter(slug=competitiontitle)
    competitionquerylist = list(CompeteModel.objects.filter(
        slug=competitiontitle).values())
    title = competitionquerylist[0]['competition_title']
    competitionid = competitionquerylist[0]['id']
    competitionproblemsqueryset = CompetitionOwnProblem.objects.filter(
        competition_id=competitionid)

    context = {
        "pagetitle": "comp",
        "details": competitionqueryset,
        "title": title,
        "slug": competitiontitle,
        "problems": competitionproblemsqueryset
    }
    return render(request, 'admin_module/viewcompetition.html', context)


@staff_member_required
@login_required
def AddCompetitionProblem(request, competitiontitle):
    competitionquerylist = list(CompeteModel.objects.filter(
        slug=competitiontitle).values())
    title = competitionquerylist[0]['competition_title']
    competitionid = competitionquerylist[0]['id']
    form = AddCompetitionProblemForm()
    context = {
        "pagetitle": "comp",
        "form": form,
        "slug": competitiontitle,
        "title": title
    }
    if request.method == 'POST':
        form = AddCompetitionProblemForm(request.POST)
        if form.is_valid():
            formdata = form.cleaned_data
            obj = form.save(commit=False)
            obj.competition_id = competitionid
            obj.save()
            messages.success(
                request, f"\"{formdata['problem_title']}\" has been successfully added for \"{title}\"")
            return redirect("ViewCompetitionDetails", competitiontitle=competitiontitle)

    return render(request, 'admin_module/addcompetitionproblem.html', context)


@staff_member_required
@login_required
def EditCompetitionProblem(request, competitiontitle, problemslug):
    competitionquerylist = list(CompeteModel.objects.filter(
        slug=competitiontitle).values())
    title = competitionquerylist[0]['competition_title']
    instance = get_object_or_404(CompetitionOwnProblem, slug=problemslug)
    form = EditCompetitionProblemForm(instance=instance)
    context = {
        "pagetitle": "comp",
        "form": form,
        "slug": competitiontitle,
        "title": title
    }
    if request.method == 'POST':
        form = AddCompetitionProblemForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            CompetitionOwnProblem.objects.filter(slug=problemslug).update(
                problem_title=form_data['problem_title'],
                problem_description=form_data['problem_description'],
                problem_statement=form_data['problem_statement'],
                problem_explanation=form_data['problem_explanation'],
                problem_constraints=form_data['problem_constraints'],
                sample_input=form_data['sample_input'],
                input_explanation=form_data['input_explanation'],
                sample_output=form_data['sample_output'],
                output_explanation=form_data['output_explanation'],
                problem_testcase_one_input=form_data['problem_testcase_one_input'],
                problem_testcase_two_input=form_data['problem_testcase_two_input'],
                problem_testcase_three_input=form_data['problem_testcase_three_input'],
                problem_testcase_one_output=form_data['problem_testcase_one_output'],
                problem_testcase_two_output=form_data['problem_testcase_two_output'],
                problem_testcase_three_output=form_data['problem_testcase_three_output'],
            )
            messages.success(
                request, f"\"{form_data['problem_title']}\" has been successfully added for \"{title}\"")
            return redirect("ViewCompetitionDetails", competitiontitle=competitiontitle)

    return render(request, 'admin_module/editcompetitionproblem.html', context)


@staff_member_required
@login_required
def DelCompetitionProblem(request, competitiontitle, problemslug):
    competitionquerylist = list(CompeteModel.objects.filter(
        slug=competitiontitle).values())
    problemquerylist = list(CompetitionOwnProblem.objects.filter(
        slug=problemslug).values())
    competitionid = competitionquerylist[0]['id']
    title = competitionquerylist[0]['competition_title']
    problemtitle = problemquerylist[0]['problem_title']
    context = {
        "pagetitle": "comp",
        "smalltitle": "Remove problem",
        "maintitle": problemtitle,
        "exp": f"\"{problemtitle}\" will be removed from the competition \"{title}\""
    }
    if request.method == 'POST':
        CompetitionOwnProblem.objects.filter(
            competition_id=competitionid).filter(slug=problemslug).delete()
        messages.success(
            request, f'\"{problemtitle}\" removed from the competition problems successfully!')
        return redirect("ViewCompetitionDetails", competitiontitle=competitiontitle)

    return render(request, 'admin_module/deletecompetitioncontent.html', context)


@staff_member_required
@login_required
def ResultListPage(request, competitiontitle, nameslug):
    profilequerylist = list(Profile.objects.filter(
        slug=nameslug).values())
    competitionquerylist = list(CompeteModel.objects.filter(
        slug=competitiontitle).values())
    competitionid = competitionquerylist[0]['id']
    title = competitionquerylist[0]['competition_title']
    userid = profilequerylist[0]['id']
    competitionprobelmresultqueryset = CompeteProblemResult.objects.filter(
        competition_id=competitionid).filter(user_id=userid)
    userquerylist = list(User.objects.filter(id=userid).values())
    username = userquerylist[0]['first_name'] + \
        " " + userquerylist[0]['last_name']
    context = {
        "results": competitionprobelmresultqueryset,
        "competitionslug": competitiontitle,
        "nameslug": nameslug,
        "pagetitle": "comp",
        "title": title,
        "username": username
    }
    return render(request, "admin_module/resultlist.html", context)


def ViewResult(request, competitiontitle, nameslug, resultslug):
    competitionprobelmresultqueryset = CompeteProblemResult.objects.filter(
        slug=resultslug)
    profilequerylist = list(Profile.objects.filter(
        slug=nameslug).values())
    competitionquerylist = list(CompeteModel.objects.filter(
        slug=competitiontitle).values())
    competitionid = competitionquerylist[0]['id']
    title = competitionquerylist[0]['competition_title']
    userid = profilequerylist[0]['id']
    competitionprobelmresultqueryset = CompeteProblemResult.objects.filter(
        competition_id=competitionid).filter(user_id=userid)
    userquerylist = list(User.objects.filter(id=userid).values())
    username = userquerylist[0]['first_name'] + \
        " " + userquerylist[0]['last_name']
    context = {
        "resultdetails": competitionprobelmresultqueryset,
        "username": username,
        "nameslug": nameslug,
        "title": title,
        "pagetitle": "comp"
    }
    return render(request, 'admin_module/viewresult.html', context)


@login_required
@staff_member_required
def InsMyProfile(request):
    if request.method == 'POST':
        UserUpdationform = UserUpdationForm(
            request.POST, instance=request.user)
        ProfileUpdationform = InsProfileUpdationForm(
            request.POST, request.FILES, instance=request.user.profile)
        if UserUpdationform.is_valid() and ProfileUpdationform.is_valid():
            UserUpdationform.save()
            ProfileUpdationform.save()
            messages.success(request, "Your information has been updated!")
            return redirect('InsMyProfile')
    else:
        blogslist = BlogModel.objects.filter(author_id=request.user.id)
        ProfileUpdationform = InsProfileUpdationForm(
            instance=request.user.institutionprofile)
        UserUpdationform = UserUpdationForm(
            instance=request.user)
        context = {
            "title": "CodeRank - My Profile",
            "ProfileUpdationform": ProfileUpdationform,
            "UserUpdationForm": UserUpdationform,
            "blogs": blogslist,
            "pagetitle": "profile"
        }
    return render(request, "admin_module/insmyprofile.html", context)


@login_required
@ staff_member_required
def ViewUser(request, nameslug):
    userdetailsqueryset = Profile.objects.filter(
        slug=nameslug)
    useridquerylist = list(Profile.objects.filter(
        slug=nameslug).values_list("user_id", flat=True))

    userid = useridquerylist[0]

    blogslist = BlogModel.objects.filter(author_id=userid)
    context = {
        "title": "CodeRank - View User",
        "userdetails": userdetailsqueryset,
        "blogs": blogslist,
        "pagetitle": "comp"
    }
    return render(request, "admin_module/viewprofile.html", context)


@login_required
@ staff_member_required
def BlogViewUser(request, nameslug):
    userdetailsqueryset = Profile.objects.filter(
        slug=nameslug)
    useridquerylist = list(Profile.objects.filter(
        slug=nameslug).values_list("user_id", flat=True))

    userid = useridquerylist[0]

    blogslist = BlogModel.objects.filter(author_id=userid)
    context = {
        "title": "CodeRank - View User",
        "userdetails": userdetailsqueryset,
        "blogs": blogslist,
        "title": "blog"
    }
    return render(request, "admin_module/viewprofile.html", context)


@login_required
@ staff_member_required
def BlogListPage(request):
    context = {
        "title": "CodeRank - Blogs",
        'blogs': BlogModel.objects.all(),
        "pagetitle": "bloglist",
        "title": "blog"
    }
    return render(request, "admin_module/bloglist.html", context)


def MyBlogListPage(request):
    context = {
        "title": "CodeRank - My Blogs",
        'blogs': BlogModel.objects.filter(author_id=request.user.id),
        "pagetitle": "mybloglist",
        "title": "blog"

    }
    return render(request, "admin_module/myblog.html", context)


def ViewBlog(request, titleslug):
    blogmodelqueryset = BlogModel.objects.filter(slug=titleslug)
    blogmodeltitlequerylist = list(BlogModel.objects.filter(
        slug=titleslug).values_list("title", flat=True))
    blogmodelauthorquerylist = list(BlogModel.objects.filter(
        slug=titleslug).values_list("author_id", flat=True))
    blogtitle = blogmodeltitlequerylist[0]
    authorqueryset = User.objects.filter(id=blogmodelauthorquerylist[0])
    context = {
        "title": "CodeRank - view blog",
        "blogcontent": blogmodelqueryset,
        "blogtitle": blogtitle,
        "authordetails": authorqueryset,
        "title": "blog"
    }
    return render(request, "admin_module/viewblog.html", context)


def PostNewBlog(request):
    if request.method == "GET":
        form = PostBlogForm()
        context = {
            "title": "CodeRank - New Blog",
            "pagetitle": "addnewblog",
            "form": form,
            "title": "blog"
        }
        return render(request, "admin_module/newblog.html", context)
    elif request.method == "POST":
        form = PostBlogForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            content = form.cleaned_data.get('content')
            BlogModel.objects.create(
                title=title, content=content, author_id=request.user.id)
            messages.success(
                request, "Blog posted successfully")
            return redirect("BlogListPage")


def EditBlog(request, titleslug):
    if request.method == "GET":
        blogdetailsquerylist = list(
            BlogModel.objects.filter(slug=titleslug).values())
        form_data = {
            "title": blogdetailsquerylist[0]["title"],
            "content": blogdetailsquerylist[0]["content"],
            "author_id": request.user.id,
        }
        form = PostBlogForm(initial=form_data)
        context = {
            "title": "CodeRank - Edit Blog",
            "form": form,
            "title": "blog"
        }
        return render(request, "admin_module/editblog.html", context)
    elif request.method == "POST":
        form = PostBlogForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            content = form.cleaned_data.get('content')
            BlogModel.objects.filter(slug=titleslug).update(
                title=title, content=content, author_id=request.user.id)
            messages.success(
                request, "Blog updated successfully")
            return redirect("BlogListPage")


@staff_member_required
@login_required
def ProblemList(request):
    practiceproblemqueryset = PracticeProblem.objects.all()
    context = {
        "title": "CodeRank - Problem",
        "problems": practiceproblemqueryset,
        "pagetitle": "prob"
    }
    return render(request, "admin_module/problemlist.html", context)


@staff_member_required
@login_required
def ViewProblem(request, problemslug):
    practiceproblemqueryset = PracticeProblem.objects.filter(slug=problemslug)
    practiceproblemquerylist = list(
        PracticeProblem.objects.filter(slug=problemslug).values())
    title = practiceproblemquerylist[0]['problem_title']

    context = {
        "title": "CodeRank - View Problem",
        "problems": practiceproblemqueryset,
        "pagetitle": "prob",
        "probtitle": title,
        "slug": problemslug
    }
    return render(request, "admin_module/viewproblem.html", context)


@staff_member_required
@login_required
def EditProblem(request, problemslug):
    instance = get_object_or_404(PracticeProblem, slug=problemslug)
    form = EditProblemForm(instance=instance)

    practiceproblemqueryset = PracticeProblem.objects.filter(slug=problemslug)
    practiceproblemquerylist = list(
        PracticeProblem.objects.filter(slug=problemslug).values())
    instanceinfo = get_object_or_404(
        ProblemInfo, problem_id=practiceproblemquerylist[0]['id'])
    forminfo = AddProblemInfoForm(instance=instanceinfo)

    title = practiceproblemquerylist[0]['problem_title']
    problem_id = practiceproblemquerylist[0]['id']
    context = {
        "title": "CodeRank - Edit Problem",
        "problems": practiceproblemqueryset,
        "pagetitle": "prob",
        "form": form,
        "probtitle": title,
        "infoform": forminfo
    }

    if request.method == "POST":
        form = EditProblemForm(request.POST)
        forminfo = EditProblemInfoForm(request.POST)
        if form.is_valid() and forminfo.is_valid():
            form_data = form.cleaned_data
            infoform_data = forminfo.cleaned_data
            PracticeProblem.objects.filter(slug=problemslug).update(
                subtopic=form_data['subtopic'],
                problem_title=form_data['problem_title'],
                problem_description=form_data['problem_description'],
                problem_statement=form_data['problem_statement'],
                problem_explanation=form_data['problem_explanation'],
                problem_constraints=form_data['problem_constraints'],
                sample_input=form_data['sample_input'],
                input_explanation=form_data['input_explanation'],
                sample_output=form_data['sample_output'],
                output_explanation=form_data['output_explanation'],
                problem_testcase_one_input=form_data['problem_testcase_one_input'],
                problem_testcase_two_input=form_data['problem_testcase_two_input'],
                problem_testcase_three_input=form_data['problem_testcase_three_input'],
                problem_testcase_one_output=form_data['problem_testcase_one_output'],
                problem_testcase_two_output=form_data['problem_testcase_two_output'],
                problem_testcase_three_output=form_data['problem_testcase_three_output'],
                difficulty=form_data['difficulty'],
            )
            ProblemInfo.objects.filter(problem_id=problem_id).update(
                tags=infoform_data['tags'],
                attempted=infoform_data['attempted'],
                accuracy=infoform_data['accuracy']
            )
            messages.success(
                request, f"\"{form_data['problem_title']}\" has been successfully updated!")
            return redirect('ViewProblem', problemslug=problemslug)
    return render(request, "admin_module/editproblem.html", context)


@staff_member_required
@login_required
def AddProblem(request):
    form = AddProblemForm()
    forminfo = AddProblemInfoForm()
    context = {
        "title": "CodeRank - Add Problem",
        "pagetitle": "prob",
        "form": form,
        "infoform": forminfo
    }

    if request.method == "POST":
        form = AddProblemForm(request.POST)
        forminfo = AddProblemInfoForm(request.POST)
        if form.is_valid() and forminfo.is_valid():
            form_data = form.cleaned_data
            form.save()
            title = form_data['problem_title']
            slugfied = slugify(title)
            problem_id = list(
                PracticeProblem.objects.filter(slug=slugfied).values())
            obj = forminfo.save(commit=False)
            obj.problem_id = problem_id[0]['id']
            obj.save()

            messages.success(
                request, f"\"{form_data['problem_title']}\" has been successfully added!")
            return redirect('ProblemList')
    return render(request, "admin_module/addproblem.html", context)


@staff_member_required
@login_required
def DelProblem(request,  problemslug):
    problemquerylist = list(PracticeProblem.objects.filter(
        slug=problemslug).values())
    problemtitle = problemquerylist[0]['problem_title']
    context = {
        "title": "CodeRank - Delete Problem",
        "pagetitle": "prob",
        "smalltitle": "Remove problem",
        "maintitle": problemtitle,
        "exp": f"\"{problemtitle}\" will be removed."
    }
    if request.method == 'POST':
        PracticeProblem.objects.filter(slug=problemslug).delete()
        messages.success(
            request, f'\"{problemtitle}\" removed from the competition problems successfully!')
        return redirect("ProblemList")

    return render(request, 'admin_module/deletecompetitioncontent.html', context)
