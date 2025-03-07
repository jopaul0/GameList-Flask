$(document).ready(function() {
    $("#openModal").click(function() {
        $("#loginModal").fadeIn();
    });

    $(".close").click(function() {
        $("#loginModal").fadeOut();
    });

    $(window).click(function(event) {
        if ($(event.target).is("#loginModal")) {
            $("#loginModal").fadeOut();
        }
    });
    $("#loginForm").submit(function(event) {
        event.preventDefault();

        let formData = new FormData(this);
        $.ajax({
            type: "POST",
            url: "/login",
            data: formData,
            processData: false,
            contentType: false,
            success: function(response) {
                if (response) {
                    location.reload();
                } else {
                    $("#mensagemLogin").html(response.mensagem);
                    $("#loginModal").fadeOut();
                    $("#erroModal").fadeIn();
                }
            },
            error: function(xhr, status, error) {
                $("#mensagemLogin").html(xhr.responseJSON.erro);
                $("#loginModal").fadeOut();
                $("#erroModal").fadeIn();
            },
        });
    });

    $(".close").click(function() {
        $("#erroModal").fadeOut();  // Fecha o modal com efeito de fade
    });

    // Fechar o modal ao clicar fora do conteúdo do modal
    $(window).click(function(event) {
        if ($(event.target).is("#erroModal")) {
            $("#erroModal").fadeOut();  // Fecha o modal ao clicar fora
        }
    });

});