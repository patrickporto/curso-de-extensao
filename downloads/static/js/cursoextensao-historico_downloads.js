var adminHistoricoDownload = adminHistoricoDownload || {};

adminHistoricoDownload = (function () {
    'use strict';

    var resultList = document.getElementById('result_list'),
        resultListBody = resultList.getElementsByTagName('tbody')[0],
        lengthOfResultList = resultListBody.getElementsByTagName('tr').length,
        paginator = document.getElementsByClassName('paginator')[0];

    function init() {
        mensagemHistoricoDownload();
    }

    function mensagemHistoricoDownload() {
        if (lengthOfResultList == 1) {
            paginator.textContent = lengthOfResultList + ' download realizado';
        } else if (lengthOfResultList == 0) {
            paginator.textContent = 'Nenhum download realizado';
        } else {
            paginator.textContent = lengthOfResultList + ' downloads realizados';
        }
    }

    return {
        init: init
    };

})();

adminHistoricoDownload.init();
