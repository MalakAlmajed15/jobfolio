from django import forms
from .models import Company, JobPosition, Application

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'website']

class JobPositionForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['job_position', 'date_applied', 'status', 'notes', 'resume']