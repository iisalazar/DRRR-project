$(document).ready(function() {
	$('.ui.dropdown').dropdown({
	    on: 'click'
    });
    $('.toc').click(function() {
        $('.ui.sidebar').sidebar('toggle')
      });
});