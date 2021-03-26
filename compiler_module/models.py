from django.contrib.auth.models import User
from django.db import models
from django.db.models.deletion import CASCADE
from rest_framework.fields import CharField
from practice_module import models as practicemodel
from django.contrib.auth.models import User


class CodeModel(models.Model):
    problem = models.ForeignKey(practicemodel.PracticeProblem, on_delete=CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    code = CharField(max_length=1000)
