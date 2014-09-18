from django.shortcuts import render


def home(request):
	return render(request, 'base.html')


def contato(request):
	return render(request, 'base.html')