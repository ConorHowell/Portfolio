from django.http import HttpResponse
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

def index(request):
    return HttpResponse("Homepage")

def contact(request):
    return render(request, 'contact.html')
def projects(request):
    return render(request, 'projects.html')
def resume(request):
    return render(request, 'resume.html')
