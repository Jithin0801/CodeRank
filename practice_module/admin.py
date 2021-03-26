from django.contrib import admin
from .models import DifficultyLevel, PracticeMainTopic, PracticeProblem, PracticeSubTopic, ProblemInfo


# Register your models here.
admin.site.register(PracticeMainTopic)
admin.site.register(PracticeSubTopic)
admin.site.register(PracticeProblem)
admin.site.register(DifficultyLevel)
admin.site.register(ProblemInfo)