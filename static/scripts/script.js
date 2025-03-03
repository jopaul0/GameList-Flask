$(document).ready(function () {
  $("#add-jogo").submit(function (e) {
    e.preventDefault();

    // Cria um novo objeto FormData para enviar os dados do formulário, incluindo arquivos
    let formData = new FormData(this);

    $.ajax({
      type: "POST",
      url: "/adicionar",
      data: formData,
      processData: false, // Impede o jQuery de processar os dados
      contentType: false, // Impede o jQuery de definir o content-type automaticamente
      success: function (response) {
        atualizar_tabela()
      },
      error: function (xhr, status, error) {
        console.error("Erro ao enviar:", error);
        alert("Erro ao enviar: " + xhr.responseText); // Exibe o erro no cliente
      },
    });
  });

  $("#foto").on("change", function () {
    let fileName = $(this).prop("files")[0]
      ? $(this).prop("files")[0].name
      : "Nenhum arquivo selecionado";
    $(".file-name").text(fileName);
  });
});

function atualizar_tabela() {
  $.ajax({
    type: "POST",
    url: "/listar",
    success: function (data) {
      $("#jogos-tuplas").html(data.tabela);
    },
  });
}
