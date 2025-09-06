from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CompanyForm, JobPositionForm, ApplicationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import Application

class SignUpView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/sign-up.html'
    
@login_required
def homepage(request):
    return render(request, 'homepage.html')

@login_required
def profile(request):
    return render(request, 'profile.html')

@login_required
def application_list(request):
    application = Application.objects.all()
    return render(request, 'application/application-list.html', {'application': application})

@login_required
def create_application(request):
    if request.method == 'POST':
        company_form = CompanyForm(request.POST)
        jobPosition_form = JobPositionForm(request.POST)
        application_form = ApplicationForm(request.POST, request.FILES)
        if company_form.is_valid() and jobPosition_form.is_valid() and application_form.is_valid():
            company = company_form.save()
            
            job = jobPosition_form.save(commit=False)
            job.company = company
            job.save()

            application = application_form.save(commit=False)
            application.user = request.user
            application.job_position = job
            application.save()
            return redirect('application_list')
        else:
            return render(request, 'application/application-form.html', {        
                'company_form': company_form,
                'jobPosition_form': jobPosition_form,
                'application_form': application_form})
    else:
        company_form = CompanyForm()
        jobPosition_form = JobPositionForm()
        application_form = ApplicationForm()       
    return render(request, 'application/application-form.html', {
        'company_form': company_form,
        'jobPosition_form': jobPosition_form,
        'application_form': application_form
    })

@login_required
def application_details(request, pk):
    application = Application.objects.get(pk=pk)
    return render(request, 'application/application-details.html', {'application': application})

@login_required
def edit_application(request, pk):
    application = Application.objects.get(pk=pk)
    company = application.job_position.company
    job = application.job_position

    if request.method == 'POST':
        company_form = CompanyForm(request.POST, instance=company)
        jobPosition_form = JobPositionForm(request.POST, instance=job)
        application_form = ApplicationForm(request.POST, request.FILES, instance=application)
        
        if company_form.is_valid() and jobPosition_form.is_valid() and application_form.is_valid():
            company_form.save()
            jobPosition_form.save()
            application_form.save()
            return redirect('application_list')
        else:
            return render(request, 'application/application-form.html', {        
                'company_form': company_form,
                'jobPosition_form': jobPosition_form,
                'application_form': application_form})
    else:
        company_form = CompanyForm(instance=company)
        jobPosition_form = JobPositionForm(instance=job)
        application_form = ApplicationForm(instance=application)       
    return render(request, 'application/application-form.html', {
        'company_form': company_form,
        'jobPosition_form': jobPosition_form,
        'application_form': application_form
    })

@login_required
def delete_application(request, pk):
    application = Application.objects.get(pk=pk)
    if request.method == 'POST':
        application.delete()
        return redirect('application_list')
    return render(request, 'application/application-details.html', {'application': application})