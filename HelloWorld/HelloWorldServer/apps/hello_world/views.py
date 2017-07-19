from django.shortcuts import render, HttpResponse

# the index function is called when root is visited
def index(request):
    response = "Hello World!"
    return HttpResponse(response)
