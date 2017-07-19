# This is the Controller
from django.shortcuts import render, HttpResponse
import datetime
# The index function is called when root is visited

# Insert your views below:
def index(request):
    i = datetime.datetime.now()
    currentDateTime = ("%s/%s/%s " % (i.day,i.month,i.year)) + (" %s:%s:%s" % (i.hour,i.month,i.second))

    context={
    "currentDateTime":currentDateTime
    }
    return render(request, 'index.html', context)
