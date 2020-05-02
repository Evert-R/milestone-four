$('body').css('padding-top', '3rem');
setTimeout(function () {
    $('.navbar').css('height', '3rem');
    $('#er-logo').slideUp(1000);
    $('.navbar').css('min-height', 'unset');
    $('.er-nav-links').css('padding-top', '0');
}, 2000)