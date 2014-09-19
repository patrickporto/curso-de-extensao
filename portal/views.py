from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages


def home(request):
    return render(request, 'base.html')


def contato(request):
    return render(request, 'base.html')


def access(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        messages.add_message(request, messages.SUCCESS, 'Usuário autenticado com sucesso!')
    else:
        messages.add_message(request, messages.ERROR, 'Usuário ou senha inválida!')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')