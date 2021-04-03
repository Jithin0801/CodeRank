from login_module.models import Profile
from django.contrib import messages
from blog_module.forms import PostBlogForm
from django.shortcuts import redirect, render
from .models import BlogModel
from django.contrib.auth.models import User

# Create your views here.


def BlogListPage(request):
    context = {
        "title": "CodeRank - Blogs",
        'blogs': BlogModel.objects.all(),
        "pagetitle": "bloglist"
    }
    return render(request, "blog_module/bloglist.html", context)


def MyBlogListPage(request):
    context = {
        "title": "CodeRank - My Blogs",
        'blogs': BlogModel.objects.filter(author_id=request.user.id),
        "pagetitle": "mybloglist"
    }
    return render(request, "blog_module/myblog.html", context)


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
        "authordetails": authorqueryset
    }
    return render(request, "blog_module/viewblog.html", context)


def PostNewBlog(request):
    if request.method == "GET":
        form = PostBlogForm()
        context = {
            "title": "CodeRank - New Blog",
            "pagetitle": "addnewblog",
            "form": form
        }
        return render(request, "blog_module/newblog.html", context)
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
            "author_id": request.user.id
        }
        form = PostBlogForm(initial=form_data)
        context = {
            "title": "CodeRank - Edit Blog",
            "form": form
        }
        return render(request, "blog_module/editblog.html", context)
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


def ViewUser(request, nameslug):
    userdetailsqueryset = Profile.objects.filter(slug=nameslug)
    useridquerylist = list(Profile.objects.filter(
        slug=nameslug).values_list("user_id", flat=True))

    userid = useridquerylist[0]

    blogslist = BlogModel.objects.filter(author_id=userid)
    context = {
        "title": "CodeRank - View User",
        "userdetails": userdetailsqueryset,
        "blogs": blogslist
    }
    return render(request, "blog_module/viewprofile.html", context)
