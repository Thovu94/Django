from django.shortcuts import render, get_object_or_404
from .models import Django_app

# Create your views here.
def function1(request):
    jobs = Django_app.objects
    return render(request, 'djangoApp/index.html', {'jobs':jobs})

def detail(request, job_id):
    job_detail = get_object_or_404(Django_app, pk=job_id)
    print(job_id)
    return render(request, 'djangoApp/detail.html', {'job': job_detail})