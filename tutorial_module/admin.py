from tutorial_module.models import MaintopicCompletedStatus, SubtopicCompletedStatus, TutorialContent, TutorialSubtopic, TutorialSubtopicCompletedStatus
from django.contrib import admin

# Register your models here.
admin.site.register(TutorialSubtopic)
admin.site.register(TutorialContent)
admin.site.register(TutorialSubtopicCompletedStatus)
admin.site.register(SubtopicCompletedStatus)
admin.site.register(MaintopicCompletedStatus)
