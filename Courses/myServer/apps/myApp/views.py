# Controller
from django.shortcuts import render, redirect
from .models import Course

# Create your views here.
def index(request):
    context = { "courses" : Course.objects.all()}
    return render(request, 'myApp/index.html', context)

def addcourse(request):
    Course.objects.create(course_name=request.POST['course_name'], description=request.POST['description'])
    return redirect('/')

def removecourse(request, id):
    context = {
        "course": Course.objects.get(id=id)
    }
    return render(request, 'myApp/remove.html', context)

def removethis(request, id):
    this = Course.objects.get(id=id)
    this.delete()
    return redirect('/')
