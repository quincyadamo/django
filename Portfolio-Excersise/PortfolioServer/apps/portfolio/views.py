from django.shortcuts import render, HttpResponse
# the index function is called when root is visited
# Controller

def index(request):
  return render(request, 'index.html')

def testimonials(request):
  return render(request, 'testimonials.html')
