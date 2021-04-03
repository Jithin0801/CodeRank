from compiler_module.models import PracticeProblemResult
from django import forms


class CodeForm(forms.ModelForm):  # Note that it is not inheriting from forms.ModelForm
    code = forms.CharField(
        widget=forms.Textarea(attrs={"id": "compilerarea"}), label="")

    class Meta:
        model = PracticeProblemResult
        fields = ['code']
