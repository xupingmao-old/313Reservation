$(function(){
	$('#menu li').click(function(){
		$('#menu li').removeClass();
		$(this).addClass('active');
	})

	$('#about').click(function(){
		window.location.href='../about';
	})

    $('#check_phone').click(function(){
		window.location.href='../check_phone';
	})

	$('#home').click(function(){
		window.location.href='/';
	})
})

