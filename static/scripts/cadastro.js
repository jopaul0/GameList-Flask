$(document).ready(function() {
    // Exibir o modal ao submeter o formulário
    $("#cadastroForm").submit(function(event) {
        event.preventDefault();

        let formData = new FormData(this);
        $.ajax({
          type: "POST",
          url: "/cadastrar",
          data: formData,
          processData: false, // Impede o jQuery de processar os dados
          contentType: false, // Impede o jQuery de definir o content-type automaticamente
          success: function (response) {
            $("#mensagemCadastro").html(response.mensagem)
            $("#myModal").fadeIn();
          },
          error: function (xhr, status, error) {
             // Exibe o erro no cliente
             $("#mensagemCadastro").html(xhr.responseJSON.erro)
            $("#myModal").fadeIn();
          },
        });
          // Exibe o modal com efeito de fade
    });

    // Fechar o modal ao clicar na "X"
    $(".close").click(function() {
        $("#myModal").fadeOut();  // Fecha o modal com efeito de fade
    });

    // Fechar o modal ao clicar fora do conteúdo do modal
    $(window).click(function(event) {
        if ($(event.target).is("#myModal")) {
            $("#myModal").fadeOut();  // Fecha o modal ao clicar fora
        }
    });
});