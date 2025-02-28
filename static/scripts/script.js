$(document).ready(function() {
    $('#add-jogo').submit(function(e) {
        e.preventDefault();
        $.ajax({
            type: 'POST',
            url: '/adicionar',
            data: $('#add-jogo').serialize(),
            success: function(response) {
                atualizar_tabela();
            }
        });
    });
});

function atualizar_tabela(){
    $.ajax({
        type: 'POST',
        url: '/listar',
        success: function(data) {
            $('#jogos-tuplas').html(data.tabela);
        }
    });
}