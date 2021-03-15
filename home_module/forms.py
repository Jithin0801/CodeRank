from django.db.models import fields
from .models import AlgorithmChallenge, DSChallenge
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.utils.translation import gettext as _

class AddDSChallengeForm(forms.ModelForm):

    class Meta:
        model = DSChallenge
        fields = ['dstitle', 'dscontent']


class AddAlgoChallengeForm(forms.ModelForm):

    class Meta:
        model = AlgorithmChallenge
        fields = ['algotitle', 'algocontent']



