from django.db import models
from typing import Text
from django.db import models
from django.db.models.fields import BooleanField, CharField
from django.db.models.fields.related import ForeignKey
from django.utils.text import slugify 

# Create your models here.


class PracticeMainTopic(models.Model):
    title = CharField(max_length=50, null=False)
    slug = models.SlugField(null=False, blank=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(PracticeMainTopic, self).save(*args, **kwargs)

class PracticeSubTopic(models.Model):
    maintopic = models.ForeignKey(
        PracticeMainTopic, on_delete=models.CASCADE)
    title = CharField(max_length=50, null=False)
    content = CharField(max_length=250, null=False)
    slug = models.SlugField(null=False, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(PracticeSubTopic, self).save(*args, **kwargs)

class PracticeProblem(models.Model):
    topic = models.ForeignKey(PracticeSubTopic, on_delete=models.CASCADE)
    problemtitle = CharField(max_length=150, null=False)
    problemexplanation = CharField(max_length=1000, null=False)
    problemcontstraints = CharField(max_length=50, null=False)
    sampleinput = CharField(max_length=500, null=False)
    sampleoutput = CharField(max_length=500, null=False)
    problemtestcaseoneinput = CharField(max_length=200, null=False)
    problemtestcasetwoinput = CharField(max_length=200, null=False)
    problemtestcasethreeinput = CharField(max_length=200, null=False)
    problemtestcaseoneoutput = CharField(max_length=200, null=False)
    problemtestcasetwooutput = CharField(max_length=200, null=False)
    problemtestcasethreeoutput = CharField(max_length=200, null=False)
    isbookmarked = BooleanField(default=False)
    slug = models.SlugField(null=False, blank=True)

    def __str__(self):
        return self.problemtitle

    def save(self, *args, **kwargs):
        self.slug = slugify(self.problemtitle)
        super(PracticeProblem, self).save(*args, **kwargs)