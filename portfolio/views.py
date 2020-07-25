from django.shortcuts import render
from .models import Project


def home(request):
    projects = Project.objects.all()

    # all our db data will be grabbed and converted into python objects by this
    # single line of code and we are sending all objts as a dict to the html page

    return render(request, 'portfolio/home.html', {'projects': projects})
    # sending the data's to html page by
    # dictionary where the key is 'projects'
