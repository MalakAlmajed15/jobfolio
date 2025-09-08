from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
    name = models.CharField(max_length=80)
    website = models.URLField(max_length=300, blank=True)

    class Meta:
        db_table = 'companies'

    def __str__(self):
        return self.name
        
class JobPosition(models.Model):
    job_position = models.CharField(max_length=50)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='positions')
    location = models.CharField(max_length=80)
    salary = models.IntegerField()

    class Meta:
        db_table = 'job_positions'

    def __str__(self):
        return self.job_position
    
class Application(models.Model):
    STATUS_CHOICES = [
        ('Applied', 'applied'), 
        ('Interviewed', 'interviewed'), 
        ('Offer', 'offer'), 
        ('Rejected', 'rejected')
        ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='applications')
    date_applied = models.DateField()
    status = models.CharField(max_length=80, choices=STATUS_CHOICES)
    notes = models.TextField(blank=True)
    resume = models.FileField(upload_to='images/', blank=True)
    job_position = models.ForeignKey(JobPosition, on_delete=models.CASCADE, related_name='applications', null=True)
    class Meta:
        db_table = 'applications'

    def __str__(self):
        return self.status
        