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
});