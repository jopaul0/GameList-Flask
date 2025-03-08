$(document).ready(function () {
  ativarEventos();

  $("#add-jogo").submit(function (e) {
    e.preventDefault();
    let formData = new FormData(this);

    $.ajax({
      type: "POST",
      url: "/adicionar",
      data: formData,
      processData: false,
      contentType: false,
      success: function (response) {
        atualizar_tabela();
      },
      error: function (xhr, status, error) {
        console.error("Erro ao enviar:", error);
        alert("Erro ao enviar: " + xhr.responseText);
      },
    });
  });

  $("#foto").on("change", function () {
    let fileName = $(this).prop("files")[0]
      ? $(this).prop("files")[0].name
      : "Nenhum arquivo selecionado";
    $("#file-name").text(fileName);
  });
  $("#edit-foto").on("change", function () {
    let fileName = $(this).prop("files")[0]
      ? $(this).prop("files")[0].name
      : "Nenhum arquivo selecionado";
    $("#file-name-edit").text(fileName);
  });

  $("#editForm").submit(function (e) {
    e.preventDefault();
    let formData = new FormData(this);

    $.ajax({
      type: "POST",
      url: "/editar",
      data: formData,
      processData: false,
      contentType: false,
      success: function (response) {
        atualizar_tabela();
      },
      error: function (xhr, status, error) {
        console.error("Erro ao enviar:", error);
        alert("Erro ao enviar: " + xhr.responseText);
      },
    });
  });
});

function ativarEventos() {
  $(document).off("click", ".jogo").on("click", ".jogo", function () {
    $("#edit-id").val($(this).data("id"));
    $("#edit-nome").val($(this).data("nome"));
    $("#edit-genero").val($(this).data("genero"));
    $("#edit-plataforma").val($(this).data("plataforma"));
    $("#edit-ano").val($(this).data("ano"));
    $("#edit-descricao").val($(this).data("descricao"));

    $("#jogoModal").fadeIn();
  });

  $(document).off("click", ".close").on("click", ".close", function () {
    $("#jogoModal").fadeOut();
  });

  $(document).off("click", "#jogoModal").on("click", "#jogoModal", function (event) {
    if ($(event.target).is("#jogoModal")) {
      $("#jogoModal").fadeOut();
    }
  });

  $(document).off("click", ".btn-delete").on("click", ".btn-delete", function () {
    let id = $('#edit-id').val();
    if (confirm("Tem certeza que deseja excluir o jogo?")) {
      $.ajax({
        type: "POST",
        url: "/excluir",
        data: { id: id },
        success: function (response) {
          atualizar_tabela();
        },
        error: function (xhr, status, error) {
          console.error("Erro ao enviar:", error);
          alert("Erro ao enviar: " + xhr.responseText);
        },
      });
    }
  });
}

function atualizar_tabela() {
  $.ajax({
    type: "POST",
    url: "/listar",
    success: function (data) {
      $("#jogos-tuplas").html(data.tabela);
      ativarEventos(); // Reaplica os eventos após a atualização
      $("#jogoModal").fadeOut();
      $("#file-name-edit").text('Nenhum arquivo selecionado');
    },
  });
}