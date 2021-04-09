from compiler_module.models import CompeteProblemResult, PracticeProblemResult, TestCaseStatus
from django.contrib import admin

# Register your models here.
admin.site.register(PracticeProblemResult)
admin.site.register(TestCaseStatus)
admin.site.register(CompeteProblemResult)