$(function(){

	food_list=[];
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
		window.location.href='/about';
	})
	$('#check_phone').click(function(){
		window.location.href='/check_phone';
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
	
	if($('#user_name').val()!=''){
		$('#start').hide();
		$('#selected-food').show();

	}else{
		$('#selected-food').hide();
		$('#order').hide()
		$('#start').show();
		$('#start').click(function(){
			window.location.href='/check_phone';
		})
	}
	
	$('.food').click(function(){
		var div=document.createElement('div')
		div.innerHTML='名称：'+$(this).attr('foodname');
		div.className='item'
		$('#selected-food')[0].appendChild(div);
		$('.item').click(function(){
			$('#selected-food')[0].removeChild($(this)[0]);
		})
		
		food_list=[]
		var foods=$('.item')
		var len=foods.length
		for(var i=0;i<len;i++){
			food_list.push(foods[i].innerHTML.substring(3,foods[i].length));
		}
	})
	
	$('#order').click(function(){
		window.location.href='/submit?food_list='+food_list;
	})
})