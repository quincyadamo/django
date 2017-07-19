from django.shortcuts import render, HttpResponse
# the index function is called when root is visited
# Controller

def index(request):
  print ("*"*50)
  return render(request, 'first_app/index.html')

def show(request):
	print request.method
	return render(request, 'first_app/showusers.html')
