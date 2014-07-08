$('#nav').affix({
      offset: {
        top: $('header').height()
      }
});	

$('#side-nav').affix({
      offset: {
        top: 200
      }
});	

/* activate scrollspy menu */
var $body   = $(document.body);
var navHeight = $('.navbar').outerHeight(true) + 10;

$body.scrollspy({
	target: '#side-nav',
	offset: navHeight
});

/* smooth scrolling sections */
$('.scroller').click(function() {
    if (location.pathname.replace(/^\//,'') == this.pathname.replace(/^\//,'') && location.hostname == this.hostname) {
      var target = $(this.hash);
      target = target.length ? target : $('[name=' + this.hash.slice(1) +']');
      if (target.length) {
        $('html,body').animate({
          scrollTop: target.offset().top - 50
        }, 1000);
        return false;
      }
    }
});