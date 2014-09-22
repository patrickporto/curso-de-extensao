from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from disciplina.models import Avaliacao, Periodo


@user_passes_test(lambda u: u.tipo == u.ALUNO)
def disciplinas(request):
    periodo_id = request.GET.get('periodo')
    context = {}
    avaliacoes = Avaliacao.objects.filter(aluno=request.user)
    context['periodos'] = Periodo.objects.filter(pk__in=avaliacoes.values('disciplina__periodo').distinct())
    if periodo_id:
        avaliacoes = avaliacoes.filter(disciplina__periodo__id=periodo_id)
        if avaliacoes.count() == 0:
            messages.add_message(request, messages.ERROR, 'O período informado não existe')

    context['periodo_id'] = periodo_id
    context['avaliacoes'] = avaliacoes
    return render(request, 'disciplinas.html', context)