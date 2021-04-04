from tutorial_module.models import TutorialSubtopicCompletedStatus
from django import forms


# Note that it is not inheriting from forms.ModelForm
class MarkAsReadForm():

    class Meta:
        model = TutorialSubtopicCompletedStatus
