var updateMask = function() {
    var field = $(this).parent().parent().parent().find('.vTextField');
    if ($(this).val() === 'telefone') {
        $(field).inputmask("(99)9999[9]-9999");
    } else {
        $(field).inputmask("remove");
    }
};

$(document).ready(function(){
    $('#id_cpf').inputmask("999.999.999-99");
    var contatoInline = $('#contato_set-group select');
    contatoInline.change(updateMask);
    contatoInline.change();
});