from compete_module.models import CompeteModel, CompetitionOwnProblem, CompetitionResult, CompetitionType, OngoingCompetition, RegisteredUserCompete, Status
from django.contrib import admin

# Register your models here.
admin.site.register(CompeteModel)
admin.site.register(CompetitionOwnProblem)
admin.site.register(RegisteredUserCompete)
admin.site.register(CompetitionResult)
admin.site.register(OngoingCompetition)
admin.site.register(Status)
admin.site.register(CompetitionType)
