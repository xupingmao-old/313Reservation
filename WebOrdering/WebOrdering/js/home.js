$(function(){
	$('#menu li').click(function(){
		$('#menu li').removeClass();
		$(this).addClass('active');
	})
	
	$('#sidebar li').click(function(){
		$('#sidebar li').removeClass();
		$(this).addClass('sidebar_active')
	})
	
	$('.food_pic img').hover(function(){
		$(this).removeClass();
		$(this).addClass('pic_show')
	}, function(){
		$(this).removeClass();
		$(this).addClass('pic_dark')
	})
})