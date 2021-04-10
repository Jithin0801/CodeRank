from django.forms.widgets import DateInput, DateTimeInput
from compete_module.models import CompeteModel, CompetitionOwnProblem, CompetitionType, RegisteredUserCompete, Status
from practice_module import models
from tutorial_module.models import TutorialContent, TutorialSubtopic
from practice_module.models import PracticeMainTopic, PracticeProblem, PracticeSubTopic
from admin_module.models import InstitutionProfile
from django.db.models import fields
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.utils.translation import gettext as _


class UserRegistrationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',
                  'email', 'password1', 'password2']


class AuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(AuthenticationForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

class AddNewMainTopicForm(forms.ModelForm):

    class Meta:
        model = PracticeMainTopic
        fields = ['title']


class AddNewSubTopicForm(forms.ModelForm):

    class Meta:
        model = PracticeSubTopic
        fields = ['title', 'content']


class UpdateMainTopicForm(forms.ModelForm):

    class Meta:
        model = PracticeMainTopic
        fields = ['title']


class UpdateSubTopicForm(forms.ModelForm):

    class Meta:
        model = PracticeSubTopic
        fields = ['title', 'content']


class DelMainTopicForm(forms.ModelForm):

    class Meta:
        model = PracticeMainTopic
        fields = ['title']


class DelSubTopicForm(forms.ModelForm):

    class Meta:
        model = PracticeSubTopic
        fields = ['title', 'content']


class EditTutorialSubTopic(forms.ModelForm):
    class Meta:
        model = TutorialSubtopic
        fields = ['title']


class DelTutorialSubTopic(forms.ModelForm):
    class Meta:
        model = TutorialSubtopic
        fields = ['subtopic', 'title']


class EditTutorialContent(forms.ModelForm):
    class Meta:
        model = TutorialContent
        fields = ['content', 'exampleone', 'exampletwo']


class AddTutorialSubTopicForm(forms.ModelForm):
    class Meta:
        model = TutorialSubtopic
        fields = ['title']

    def __init__(self, *args, **kwargs):
        super(AddTutorialSubTopicForm, self).__init__(*args, **kwargs)
        self.fields['subtopic_id'] = forms.ModelChoiceField(
            queryset=PracticeSubTopic.objects.all(), empty_label="Select subtopic")


class AddTutorialContentForm(forms.ModelForm):
    class Meta:
        model = TutorialContent
        fields = ['content', 'exampleone', 'exampletwo']


class AddCompetitionForm(forms.ModelForm):
    class Meta:
        model = CompeteModel
        fields = ['competition_title', 'competition_description',
                  'registration_start_date', 'registration_end_date', 'competition_start_date', 'competition_end_date', 'assessment_time']
        widgets = {
            'registration_start_date': DateTimeInput(attrs={'type': 'datetime-local'}),
            'registration_end_date': DateTimeInput(attrs={'type': 'datetime-local'}),
            'competition_start_date': DateTimeInput(attrs={'type': 'datetime-local'}),
            'competition_end_date': DateTimeInput(attrs={'type': 'datetime-local'})
        }
  

    def __init__(self, *args, **kwargs):
        super(AddCompetitionForm, self).__init__(*args, **kwargs)
        self.fields['type_id'] = forms.ModelChoiceField(
            queryset=CompetitionType.objects.all(), empty_label="Select competition type")
        self.fields['status_id'] = forms.ModelChoiceField(
            queryset=Status.objects.all(), empty_label="Select competition status")


class DelCompetitionForm(forms.ModelForm):
    class Meta:
        model = CompeteModel
        fields = ['competition_title', 'competition_description',
                  'registration_start_date', 'registration_end_date', 'competition_start_date', 'competition_end_date', 'assessment_time']


class EditCompetitionForm(forms.ModelForm):
    class Meta:
        model = CompeteModel
        fields = ['competition_title', 'competition_description',
                  'registration_start_date', 'registration_end_date', 'competition_start_date', 'competition_end_date', 'assessment_time','status','type']
        widgets = {
            'registration_start_date': DateTimeInput(attrs={'type': 'datetime-local'}),
            'registration_end_date': DateTimeInput(attrs={'type': 'datetime-local'}),
            'competition_start_date': DateTimeInput(attrs={'type': 'datetime-local'}),
            'competition_end_date': DateTimeInput(attrs={'type': 'datetime-local'})
        }

class DelRegisteredUserForm(forms.ModelForm):
    class Meta:
        model = RegisteredUserCompete
        fields = ['registeredon', 'competition', 'user']

class AddCompetitionProblemForm(forms.ModelForm):
    class Meta:
        model = CompetitionOwnProblem
        exclude = ['slug','competition']


class EditCompetitionProblemForm(forms.ModelForm):
    class Meta:
        model = CompetitionOwnProblem
        exclude = ['slug', 'competition']


class DelCompetitionProblemForm(forms.ModelForm):
    class Meta:
        model = CompetitionOwnProblem
        exclude = ['slug', 'competition']


class UserUpdationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',
                  'email']


class InsProfileUpdationForm(forms.ModelForm):

    image = forms.ImageField(label=_('Profile Picture'), required=False, error_messages={
                             'invalid': _("Image files only")}, widget=forms.FileInput)

    class Meta:
        model = InstitutionProfile
        fields = ['institution_name', 'bio', 'address', 'phone_number', 'image']


class AddProblemForm(forms.ModelForm):
    class Meta:
        model = PracticeProblem
        exclude = ['isbookmarked', 'slug']



class EditProblemForm(forms.ModelForm):
    class Meta:
        model = PracticeProblem
        exclude = ['isbookmarked', 'slug']
