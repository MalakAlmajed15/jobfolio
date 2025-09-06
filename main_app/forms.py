from django import forms
from .models import Company, JobPosition, Application

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'website']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Company Name'}),
            'website': forms.URLInput(attrs={'placeholder': 'https://example.com'}),
        }

class JobPositionForm(forms.ModelForm):
    class Meta:
        model = JobPosition
        fields = ['location', 'salary']

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['job_position', 'date_applied', 'status', 'notes', 'resume']