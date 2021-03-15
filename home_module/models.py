from django.db import models
from django.db.models.fields import CharField

class DSChallenge(models.Model):
    dstitle = CharField(max_length=50, null=False)
    dscontent = CharField(max_length=250, null=False)

    def __str__(self):
        return self.dstitle

class AlgorithmChallenge(models.Model):
    algotitle = CharField(max_length=50, null=False)
    algocontent = CharField(max_length=250, null=False)

    def __str__(self):
        return self.algotitle