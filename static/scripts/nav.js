$(() => {
    $(".nav-btn").click(() => {
        $(".nav").addClass("nav-open");
    });

    $(".nav-close").click(() => {
        $(".nav").removeClass("nav-open");
    });
});