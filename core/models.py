# -*- encoding: utf-8 -*-
FOTOS = 1
CURRICULO = 2
HISTORICO_SUPERIOR = 3
RG = 4
TITULO_ELEITOR = 5
CERTIFICADO_RESERVISTA = 6
DIPLOMA_GRADUACAO = 7

CHOICES_DOCUMENTOS = (
    (FOTOS, '2 fotos 3x4',),
    (CURRICULO, 'Currículo',),
    (HISTORICO_SUPERIOR, 'Histórico Nível Superior',),
    (RG, 'Carteira Identidade',),
    (TITULO_ELEITOR, 'Título de Eleitor',),
    (CERTIFICADO_RESERVISTA, 'Certificado de Reservista',),
    (DIPLOMA_GRADUACAO, 'Diploma de Graduação',),
)

get_documento_display = lambda v: dict(CHOICES_DOCUMENTOS)[v]
