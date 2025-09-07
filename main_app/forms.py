from django import forms
from .models import Company, JobPosition, Application

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'website']
        labels = {
            'name': 'Company Name',
            'website': 'Company Website'
        }

class JobPositionForm(forms.ModelForm):
    class Meta:
        model = JobPosition
        fields = ['job_position', 'location', 'salary']
        labels = {
            'job_position': 'Job Position',
            'location': 'Company Location',
            'salary': 'Salary'
        }

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['date_applied','status', 'notes', 'resume']
        labels = {
            'date_applied': 'Date Applied',
            'status': 'Application Status',
            'notes': 'Additional Notes',
            'resume': 'Upload Resume'
        }
        widgets = {
            'date_applied': forms.DateInput(attrs={'type': 'date'}),
        }