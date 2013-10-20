$(function(){
	$('#menu li').click(function(){
		$('#menu li').removeClass();
		$(this).addClass('active');
	})
	
	$('#sidebar li').click(function(){
		$('#sidebar li').removeClass();
		$(this).addClass('sidebar_active')
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
