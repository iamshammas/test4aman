from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    students = [{
        'name':"AMAL JOY",
        'age':22,
        'job':'Software Engineer',
        'place' : 'kochi'
    }]
    return HttpResponse(students)