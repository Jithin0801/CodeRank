from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField, IntegerField, TextField
from django.utils import timezone
from practice_module import models as practice_model
from django.utils.text import slugify

# Create your models here.


class Status(models.Model):
    status = models.CharField(max_length=20, null=False, default="Upcoming")

    def __str__(self):
        return self.status


class CompetitionType(models.Model):
    type = models.CharField(max_length=20, null=False,
                            default="Coding Competition")

    def __str__(self):
        return self.type


class CompeteModel(models.Model):
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    competitiontitle = models.CharField(max_length=100)
    competitiondescription = models.TextField(max_length=3000)
    regstartdate = models.DateTimeField(null=False)
    regenddate = models.DateTimeField(null=False)
    competitionstartdate = models.DateTimeField(null=False)
    competitionenddate = models.DateTimeField(null=False)
    assessmenttime = models.IntegerField(default=10, null=False)
    date_posted = models.DateTimeField(default=timezone.now)
    status = models.ForeignKey(Status, on_delete=CASCADE, default=1)
    type = models.ForeignKey(CompetitionType, on_delete=CASCADE, default=1)
    slug = models.SlugField(null=False, blank=True)

    def __str__(self):
        return self.competitiontitle

    def save(self, *args, **kwargs):
        self.slug = slugify(self.competitiontitle)
        super(CompeteModel, self).save(*args, **kwargs)


class CompetitionOwnProblem(models.Model):
    competition = models.ForeignKey(CompeteModel, on_delete=CASCADE)
    problemtitle = CharField(max_length=150, null=False)
    problemdescription = TextField(max_length=1000, null=False)
    problemstatement = TextField(max_length=1000, null=False)
    problemexplanation = TextField(max_length=1000, null=False)
    problemconstraints = TextField(max_length=500, null=False)
    sampleinput = TextField(max_length=500, null=False)
    inputexplanation = TextField(max_length=1000, null=False)
    sampleoutput = TextField(max_length=500, null=False)
    outputexplanation = TextField(max_length=1000, null=False)
    problemtestcaseoneinput = TextField(max_length=200, null=False)
    problemtestcasetwoinput = TextField(max_length=200, null=False)
    problemtestcasethreeinput = TextField(max_length=200, null=False)
    problemtestcaseoneoutput = TextField(max_length=200, null=False)
    problemtestcasetwooutput = TextField(max_length=200, null=False)
    problemtestcasethreeoutput = TextField(max_length=200, null=False)
    score = IntegerField(default=20, null=False)
    slug = models.SlugField(max_length=100,  null=False, blank=True)

    def __str__(self):
        return self.problemtitle

    def save(self, *args, **kwargs):
        self.slug = slugify(self.problemtitle)
        super(CompetitionOwnProblem, self).save(*args, **kwargs)


class RegisteredUserCompete(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    competition = models.ForeignKey(CompeteModel, on_delete=CASCADE)
    registeredon = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user.first_name


class OngoingCompetition(models.Model):
    competition = models.ForeignKey(CompeteModel, on_delete=CASCADE)
    starttime = models.DateTimeField(null=False),
    endtime = models.DateTimeField(null=False)


class CompetitionResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    competition = models.ForeignKey(CompeteModel, on_delete=CASCADE)
    score = models.IntegerField(default=0, null=False)
    completedon = models.DateTimeField(default=timezone.now)
    timetaken = models.IntegerField(default=0, null=False)
