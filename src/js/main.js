jQuery(document).ready(function ($) {
    $('#tabs').tab();
    $('.scroll-tab').scrollspy('refresh');
});
    
$(function() {
    $('#tabs li a').bind('click', function (e) {
        $('.scroll-tab').scrollspy('refresh');
        $('.scroll-tab').scrollspy('process');
    });
});