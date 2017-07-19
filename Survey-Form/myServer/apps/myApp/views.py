# This is the Controller
from django.shortcuts import render, redirect

def index(request):
	return render(request, 'index.html')


def process(request):
	if 'counter' in request.session:
		request.session['counter'] +=1
	else:
		request.session['counter'] = 1

	request.session['data'] = {
		'f_name': request.POST['f_name'],
		'dojoLocation': request.POST['dojoLocation'],
		'favlang': request.POST['favlang'],
		'comments': request.POST['comments'],
	}

	return redirect('/results')


def results(request):
	print 'The Results'
	print request.session
	return render(request, 'results.html')
