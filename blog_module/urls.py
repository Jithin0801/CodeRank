from django.urls import path
from . import views

urlpatterns = [
    path("blogs/", views.BlogListPage, name="BlogListPage"),
    path("myblogs/", views.MyBlogListPage, name="MyBlogListPage"),
    path("newblog/", views.PostNewBlog, name="PostNewBlog"),
    path("blogs/<slug:titleslug>", views.ViewBlog, name="ViewBlog"),
    path("blogs/<slug:titleslug>/edit", views.EditBlog, name="EditBlog"),
    path("user/<slug:nameslug>/", views.ViewUser, name="ViewUser"),


]
