from django import forms
from .models import Company, JobPosition, Application

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'website']