from django.db.models.deletion import CASCADE
from practice_module.models import PracticeMainTopic, PracticeSubTopic
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.


class TutorialSubtopic(models.Model):
    subtopic = models.ForeignKey(PracticeSubTopic, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=False)
    slug = models.SlugField(null=False, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(TutorialSubtopic, self).save(*args, **kwargs)


class TutorialContent(models.Model):
    tutorialsubtopic = models.ForeignKey(TutorialSubtopic, on_delete=CASCADE)
    content = models.TextField(max_length=2000, null=False)
    exampleone = models.TextField(max_length=2000, null=False)
    exampletwo = models.TextField(max_length=2000, null=False)

    def __str__(self):
        return self.tutorialsubtopic.title


class TutorialSubtopicCompletedStatus(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    tutorialsubtopic = models.ForeignKey(TutorialSubtopic, on_delete=CASCADE)
    iscompleted = models.BooleanField(default=0, null=False)

    def __str__(self):
        return self.tutorialsubtopic.title


class SubtopicCompletedStatus(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    subtopic = models.ForeignKey(PracticeSubTopic, on_delete=CASCADE)
    iscompleted = models.BooleanField(default=0, null=False)

    def __str__(self):
        return self.subtopic.title


class MaintopicCompletedStatus(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    maintopic = models.ForeignKey(PracticeMainTopic, on_delete=CASCADE)
    iscompleted = models.BooleanField(default=0, null=False)

    def __str__(self):
        return self.maintopic.title
