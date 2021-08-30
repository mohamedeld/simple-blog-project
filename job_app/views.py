from django.shortcuts import render
from .models import Job
# Create your views here.
def home(request):
    jobs = Job.objects.all()
    return render(request,'job_app/home.html',{
        'jobs':jobs
    })
