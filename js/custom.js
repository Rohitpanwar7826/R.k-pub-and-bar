(function($) {
    "use strict";
	
	
	$(window).on('load', function() { 
		$('.preloader').fadeOut(); 
		$('#preloader').delay(1050).fadeOut('slow'); 
		$('body').delay(950).css({'overflow':'visible'});
	});
}(jQuery));