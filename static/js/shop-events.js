$('#er-slide').slideUp();
$('#er-hover-slide').hover(function () {
    $('#er-slide').slideDown(500)
});
$('#er-hover-slide').mouseleave(function () {
    $('#er-slide').slideUp(500)
});