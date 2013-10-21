$(function(){
	$('#menu li').click(function(){
		$('#menu li').removeClass();
		$(this).addClass('active');
	})
	
	$('.login_form_input').click(function(){
		$('#menu li').removeClass();
		$(this).addClass('active');
	})
	
	$('#check_phone').click(function(){
		window.location.href='../check_phone';
	})

	$('#home').click(function(){
		window.location.href='/';
	})
	
})

function addLoadEvent (func) {
	var oldonload = window.oldload;
	if (typeof window.onload != 'function') {
		window.onload = func;
	}else{
		window.onload = function({
			oldonload();
			func();
		}
	}
}
