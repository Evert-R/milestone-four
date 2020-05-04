window.onload = function () {
    $('.nav-item').on('click', function () {
        $('.nav-item').removeClass('active');
        $(this).addClass('active');
    })
    setTimeout(function () {
        $('.er-messages').slideUp(1000);
    }, 2000);
}