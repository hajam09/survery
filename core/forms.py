from django import forms

from core.models import Survey


class SurveyForm(forms.ModelForm):
    class Meta:
        model = Survey
        fields = ['title', 'description', 'isActive']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'isActive': forms.CheckboxInput(attrs={'class': 'form-check-input big-checkbox'}),
        }
