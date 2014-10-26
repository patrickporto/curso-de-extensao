$(document).ready(function(){
    var navPendencia = $('a[href$="/perfil/pendencias/"]'),
        breadcrumbPendencia = $("ol.breadcrumb li:contains('Pendencias')"),
        correctForm = 'Pendências';

    if (navPendencia){navPendencia.text(correctForm);}
    if (breadcrumbPendencia){ breadcrumbPendencia.text(correctForm);}
});
