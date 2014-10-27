# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.conf import settings
from disciplina.models import Avaliacao
from pessoa.models import Pessoa


def home(request):
    return render(request, 'base.html')


def witty(request):
    context = {'link': settings.IFRAME_URL}
    return render(request, 'witty.html', context)


# from disciplina.models import Periodo

# @user_passes_test(lambda u: u.tipo == u.ALUNO)
# def disciplinas(request):
#     periodo_id = int(request.GET.get('periodo', 0))
#     context = {}
#     avaliacoes = Avaliacao.objects.filter(aluno=request.user)
#     periodos = Periodo.objects.filter(pk__in=avaliacoes.values('disciplina__periodo').distinct())
#     if periodo_id:
#         avaliacoes = avaliacoes.filter(disciplina__periodo__id=periodo_id)
#     if avaliacoes.count() == 0 and periodo_id:
#         messages.add_message(request, messages.ERROR, 'O período informado não existe')

#     context['periodo_id'] = periodo_id
#     context['avaliacoes'] = avaliacoes
#     context['periodos'] = periodos

#     return render(request, 'disciplinas.html', context)


@user_passes_test(lambda u: u.tipo == u.FUNCIONARIO)
def historicos(request):
    context = {}
    aluno_id = int(request.GET.get('aluno', 0))
    alunos_pk_list = Avaliacao.objects.values_list('aluno__pk').distinct()
    alunos = Pessoa.objects.filter(id__in=alunos_pk_list)
    historicos = Avaliacao.objects.all()

    if aluno_id:
        historicos = historicos.filter(aluno__id=aluno_id)
    if historicos.count() == 0 and aluno_id:
        messages.add_message(request, messages.ERROR, 'O aluno informado não existe')

    context['aluno_id'] = aluno_id
    context['alunos'] = alunos
    context['historicos'] = historicos
    return render(request, 'historico.html', context)


def access(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    if not username:
        messages.add_message(request, messages.ERROR, 'O CPF do usuário é obrigatório')
    elif not password:
        messages.add_message(request, messages.ERROR, 'A senha do usuário é obrigatória')
    else:
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            # messages.add_message(request, messages.SUCCESS, 'Usuário autenticado com sucesso!')
        else:
            messages.add_message(request, messages.ERROR, 'Usuário ou senha inválida!')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def user_logout(request):
    logout(request)
    # messages.add_message(request, messages.WARNING, 'Você desconectou-se')
    return HttpResponseRedirect('/')


@login_required
def alterar_senha(request):
    form = PasswordChangeForm(request.user, request.POST or None)
    if request.POST:
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Sua senha foi alterada com sucesso. Por favor, autentique-se novamente')
            return HttpResponseRedirect('/')

    return render(request, 'change_password.html', {'form': form})
