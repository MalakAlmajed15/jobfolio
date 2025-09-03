from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Company, JobPosition, Application
from .forms import CompanyForm, JobPositionForm, ApplicationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

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
def create_application(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_Valid():
            form.save()
            return redirect('homepage')
        else:
            return render(request, 'application/application-form.html', {'form': form})
    else:
        form = ApplicationForm()
    return render(request, 'application/application-form.html', {'form': form})

