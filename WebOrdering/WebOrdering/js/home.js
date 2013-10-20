$(function(){
	$('.food').hide();
	$('.food[category="taocan"]').show();
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
	
	$('#about').click(function(){
		window.location.href='about';
	})
	
	$('#sidebar ul li').click(function(){
		$('.food').hide();
		if($(this).text()=='超值套餐'){
			$('.food[category="taocan"]').show();
		}
		else if($(this).text()=='经典盖饭'){
			$('.food[category="gaifan"]').show();
		}
		else if($(this).text()=='小吃点心'){
			$('.food[category="dianxin"]').show();
		}
		else if($(this).text()=='饮品'){
			$('.food[category="yinpin"]').show();
		}
	})
})