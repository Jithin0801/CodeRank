from django.db import models
from typing import Text
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import BooleanField, CharField, IntegerField, TextField
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
    content = TextField(max_length=250, null=False)
    slug = models.SlugField(null=False, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(PracticeSubTopic, self).save(*args, **kwargs)


class DifficultyLevel(models.Model):
    difficulty = CharField(max_length=15, null=False)

    def __str__(self):
        return self.difficulty


class PracticeProblem(models.Model):
    subtopic = models.ForeignKey(PracticeSubTopic, on_delete=models.CASCADE)
    problem_title = CharField(max_length=150, null=False)
    problem_description = TextField(max_length=1000, null=False)
    problem_statement = TextField(max_length=1000, null=False)
    problem_explanation = TextField(max_length=1000, null=False)
    problem_constraints = TextField(max_length=50, null=False)
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
    isbookmarked = BooleanField(default=False)
    difficulty = models.ForeignKey(DifficultyLevel, on_delete=CASCADE)
    score = IntegerField(default=20, null=False)
    slug = models.SlugField(null=False, blank=True)

    def __str__(self):
        return self.problem_title 

    def save(self, *args, **kwargs):
        self.slug = slugify(self.problem_title)
        super(PracticeProblem, self).save(*args, **kwargs)


class ProblemInfo(models.Model):
    problem = models.ForeignKey(PracticeProblem, on_delete=CASCADE)
    tags = models.CharField(default="null", max_length=250, null=False)
    attempted = IntegerField(default=0, null=False)
    accuracy = IntegerField(default=0, null=False)

    def __str__(self):
        return self.problem.problem_title
