from django.contrib import admin
from .models import PracticeMainTopic, PracticeProblem, PracticeSubTopic


# Register your models here.
admin.site.register(PracticeMainTopic)
admin.site.register(PracticeSubTopic)
admin.site.register(PracticeProblem)