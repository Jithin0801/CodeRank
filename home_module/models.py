from typing import Text
from django.db import models
from django.db.models.fields import CharField
from django.db.models.fields.related import ForeignKey

class DSTopic(models.Model):
    dstitle = CharField(max_length=50, null=False)
    dscontent = CharField(max_length=250, null=False)

    def __str__(self):
        return self.dstitle

class AlgorithmTopic(models.Model):
    algotitle = CharField(max_length=50, null=False)
    algocontent = CharField(max_length=250, null=False)

    def __str__(self):
        return self.algotitle


class DSProblem(models.Model):
    topic = models.ForeignKey(DSTopic ,on_delete=models.CASCADE)
    problemtitle = CharField(max_length=150, null=False)
    problemexplanation = CharField(max_length=1000, null=False)
    problemcontstraints = CharField(max_length=50, null=False)
    sampleinput = CharField(max_length=500, null=False)
    sampleoutput = CharField(max_length=500, null=False)
    
class AlgoProblem(models.Model):
    topic = models.ForeignKey(AlgorithmTopic)
    problemtitle = CharField(max_length=150, null=False)
    problemexplanation = CharField(max_length=1000, null=False)
    problemcontstraints = CharField(max_length=50, null=False)
    sampleinput = CharField(max_length=500, null=False)
    sampleoutput = CharField(max_length=500, null=False)


class TestCase(models.Model):
    problemtopic = models.ForeignKey(DSProblem)
    problemtestcaseoneinput = CharField(max_length=200, null=False)
    problemtestcasetwoinput = CharField(max_length=200, null=False)
    problemtestcasethreeinput = CharField(max_length=200, null=False)
    problemtestcasefourinput = CharField(max_length=200, null=False)
    problemtestcasefiveinput = CharField(max_length=200, null=False)
    problemtestcaseoneoutput = CharField(max_length=200, null=False)
    problemtestcasetwooutput = CharField(max_length=200, null=False)
    problemtestcasethreeoutput = CharField(max_length=200, null=False)
    problemtestcasefouroutput = CharField(max_length=200, null=False)
    problemtestcasefiveoutput = CharField(max_length=200, null=False)


