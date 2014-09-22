from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from disciplina.models import Avaliacao, Periodo


@user_passes_test(lambda u: u.tipo == u.ALUNO)
def disciplinas(request):
    periodo_id = int(request.GET.get('periodo', 0))
    context = {}
    avaliacoes = Avaliacao.objects.filter(aluno=request.user)
    periodos = Periodo.objects.filter(pk__in=avaliacoes.values('disciplina__periodo').distinct())
    if periodo_id:
        avaliacoes = avaliacoes.filter(disciplina__periodo__id=periodo_id)
    else:
        avaliacoes = avaliacoes.filter(disciplina__periodo=periodos.last())
    if avaliacoes.count() == 0 and periodo_id:
        messages.add_message(request, messages.ERROR, 'O período informado não existe')

    context['periodo_id'] = periodo_id
    context['avaliacoes'] = avaliacoes
    context['periodos'] = periodos
    return render(request, 'disciplinas.html', context)