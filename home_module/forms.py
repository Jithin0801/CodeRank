from django.db.models import fields
from .models import AlgorithmTopic, DSTopic
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.utils.translation import gettext as _

class AddDSChallengeForm(forms.ModelForm):

    class Meta:
        model = DSTopic
        fields = ['dstitle', 'dscontent']


class AddAlgoChallengeForm(forms.ModelForm):

    class Meta:
        model = AlgorithmTopic
        fields = ['algotitle', 'algocontent']



