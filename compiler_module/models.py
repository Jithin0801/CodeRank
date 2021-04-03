from django.contrib.auth.models import User
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import BooleanField, CharField, IntegerField
from django.db.models.fields.related import ForeignKey
from practice_module import models as practicemodel
from django.contrib.auth.models import User


class TestCaseStatus(models.Model):
    status = CharField(max_length=20, null=False)

    def __str__(self):
        return self.status


class PracticeProblemResult(models.Model):
    problem = models.ForeignKey(
        practicemodel.PracticeProblem, on_delete=CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    useroutputone = CharField(max_length=20, null=False)
    useroutputtwo = CharField(max_length=20, null=False)
    useroutputthree = CharField(max_length=20, null=False)
    useroutputonestatus = models.ForeignKey(
        TestCaseStatus, related_name="outputstatusone", on_delete=CASCADE)
    useroutputtwostatus = models.ForeignKey(
        TestCaseStatus, related_name="outputstatustwo", on_delete=CASCADE)
    useroutputthreestatus = models.ForeignKey(
        TestCaseStatus, related_name="outputstatusthree", on_delete=CASCADE)
    score = IntegerField(default=0, null=False)
    code = CharField(max_length=5000)

    def __str__(self):
        return self.problem.problemtitle