from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage
from downloads.models import Arquivo

def _get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def download(request, slug):
    arquivo = get_object_or_404(Arquivo, slug=slug)
    arquivo.downloads += 1
    arquivo.save()
    arquivo.registre(request.user, _get_client_ip(request))
    response = HttpResponse(arquivo.arquivo)
    response['Content-Disposition'] = 'attachment; filename={0}'.format(arquivo.arquivo.name[2:])
    return response

def arquivos(request):
    page = request.GET.get('page', 1)
    q = request.GET.get('q', '')

    qs = Arquivo.objects.pesquisa(q)
    paginator = Paginator(qs, 25)
    try:
        lista_arquivos = paginator.page(page)
    except EmptyPage:
        lista_arquivos = paginator.page(paginator.num_pages)

    return render(request, 'arquivos.html', {'arquivos': lista_arquivos, 'q': q})