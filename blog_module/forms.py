from blog_module.models import BlogModel
from django import forms
from django.contrib.auth.models import User
from django.db import models
from django.db.models import fields


class PostBlogForm(forms.ModelForm):

    class Meta:
        model = BlogModel
        fields = ['title', 'content']
