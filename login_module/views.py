from blog_module.models import BlogModel
from login_module.models import Profile
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render
from .forms import UserRegistrationForm, UserUpdationForm, ProfileUpdationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def HomePage(request):
    return render(request, "login_module/home.html")


def DevSignUpPage(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Account created for { username }, Now login!')
            return redirect("DevLogIn")
        else:
            pass
    else:
        form = UserRegistrationForm()
    return render(request, "login_module/devsignup.html", {"title": "CodeRank - Sign Up", "form": form})


def DevLogIn(request):
    if request.method == "POST":
        form = AuthenticationForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active:
                form = login(request, user)
                try:
                    user.profile
                except:
                    return redirect('AccountSetUp')
                else:
                    return redirect('DevHome')

            else:
                username = form.cleaned_data.get('username')
                messages.error(
                    request, f'Account { username } is inactive, Please contact the admin')
        else:
            messages.error(
                request, "Username or Password is incorrect")

    form = AuthenticationForm()
    return render(request, "login_module/devlogin.html", {"title": "CodeRank - Log In", "form": form})


@login_required
def DevMyProfile(request):
    if request.method == 'POST':
        UserUpdationform = UserUpdationForm(
            request.POST, instance=request.user)
        ProfileUpdationform = ProfileUpdationForm(
            request.POST, request.FILES, instance=request.user.profile)
        if UserUpdationform.is_valid() and ProfileUpdationform.is_valid():
            UserUpdationform.save()
            ProfileUpdationform.save()
            messages.success(request, "Your information has been updated!")
            return redirect('DevMyProfile')
    else:
        blogslist = BlogModel.objects.filter(author_id=request.user.id)
        ProfileUpdationform = ProfileUpdationForm(
            instance=request.user.profile)
        UserUpdationform = UserUpdationForm(
            instance=request.user)
        context = {"title": "CodeRank - My Profile",
                   "ProfileUpdationform": ProfileUpdationform,
                   "UserUpdationForm": UserUpdationform,
                   "blogs": blogslist
                   }
    return render(request, "login_module/devmyprofile.html", context)


@login_required
def CompleteYourProfile(request):
    if request.method == 'POST':
        profile = Profile.objects.create(user=request.user)
        UserUpdationform = UserUpdationForm(
            request.POST, instance=request.user)
        ProfileUpdationform = ProfileUpdationForm(
            request.POST, request.FILES, instance=request.user.profile)
        if UserUpdationform.is_valid() and ProfileUpdationform.is_valid():
            UserUpdationform.save()
            ProfileUpdationform.save()
            messages.success(request, "Your information has been updated!")
            return redirect('DevHome')
    else:
        ProfileUpdationform = ProfileUpdationForm()
        UserUpdationform = UserUpdationForm(instance=request.user)
    return render(request, "login_module/completeYourProfile.html", {"title": "Welcome-Complete your profile", "ProfileUpdationform": ProfileUpdationform, "UserUpdationForm": UserUpdationform})
