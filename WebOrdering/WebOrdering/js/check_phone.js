$(function(){
	$('#menu li').click(function(){
		$('#menu li').removeClass();
		$(this).addClass('active');
		window.location.href="login.jsp?backurl="+window.location.href;
	})
	
	$('.login_form_input').click(function(){
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
		window.location.href='../';
	})
})

