from django.db.models import fields
from .models import Profile
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


class UserUpdationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name',
                  'email']


class ProfileUpdationForm(forms.ModelForm):

    image = forms.ImageField(label=_('Profile Picture'),required=False, error_messages = {'invalid':_("Image files only")}, widget=forms.FileInput)


    class Meta:
        model = Profile
        fields = ['bio', 'work_experience', 'image']
