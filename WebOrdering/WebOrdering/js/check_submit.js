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