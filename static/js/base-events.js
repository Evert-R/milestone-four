// Make clicked nav button active

window.onload = function () {
    $('.nav-item').on('click', function () {
        $('.nav-item').removeClass('active');
        $(this).addClass('active');

    });
};

// Slide up error/success messages
setTimeout(function () {
    $('.er-messages').slideUp(1000);
}, 2000);

/* 
When scrolled up, the footer is sticky
and only shows the artist links when viewed on mobile
because otherwise it will fill up to much screen
When we scroll down the footer jumps to the bottom of the page
so it's not too intrusive
*/

$(window).scroll(function () {
    if ($(this).scrollTop() > 0) {
        $('.er-footer').css('position', 'unset');
        $('.er-web').removeClass('er-web-display');
    } else {
        $('.er-footer').css('position', 'fixed');
        $('.er-web').addClass('er-web-display');
    }
});
