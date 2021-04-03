from django.db import models
from django.contrib.auth.models import User
from django.http import request
from django.utils import timezone
from django.utils.text import slugify

# Create your models here.


class BlogModel(models.Model):
    title = models.CharField(max_length=1000)
    content = models.TextField(max_length=5000)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=500, null=False, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        self.date_posted = timezone.now()
        super(BlogModel, self).save(*args, **kwargs)
