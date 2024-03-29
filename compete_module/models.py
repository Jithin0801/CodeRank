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
    competition_title = models.CharField(max_length=100)
    competition_description = models.TextField(max_length=3000)
    registration_start_date = models.DateTimeField(null=False)
    registration_end_date = models.DateTimeField(null=False)
    competition_start_date = models.DateTimeField(null=False)
    competition_end_date = models.DateTimeField(null=False)
    assessment_time = models.IntegerField(default=10, null=False)
    date_posted = models.DateTimeField(default=timezone.now)
    status = models.ForeignKey(Status, on_delete=CASCADE, default=1)
    type = models.ForeignKey(CompetitionType, on_delete=CASCADE, default=1)
    slug = models.SlugField(null=False, blank=True)

    def __str__(self):
        return self.competition_title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.competition_title)
        super(CompeteModel, self).save(*args, **kwargs)


class CompetitionOwnProblem(models.Model):
    competition = models.ForeignKey(CompeteModel, on_delete=CASCADE)
    problem_title = CharField(max_length=150, null=False)
    problem_description = TextField(max_length=1000, null=False)
    problem_statement = TextField(max_length=1000, null=False)
    problem_explanation = TextField(max_length=1000, null=False)
    problem_constraints = TextField(max_length=500, null=False)
    sample_input = TextField(max_length=500, null=False)
    input_explanation = TextField(max_length=1000, null=False)
    sample_output = TextField(max_length=500, null=False)
    output_explanation = TextField(max_length=1000, null=False)
    problem_testcase_one_input = TextField(max_length=200, null=False)
    problem_testcase_two_input = TextField(max_length=200, null=False)
    problem_testcase_three_input = TextField(max_length=200, null=False)
    problem_testcase_one_output = TextField(max_length=200, null=False)
    problem_testcase_two_output = TextField(max_length=200, null=False) 
    problem_testcase_three_output = TextField(max_length=200, null=False)
    score = IntegerField(default=20, null=False)
    slug = models.SlugField(max_length=100,  null=False, blank=True)

    def __str__(self):
        return self.problem_title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.problem_title)
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
