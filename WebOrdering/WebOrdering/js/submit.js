$(function(){
	text=window.location.href;
	user_name=''
	var startpos=text.indexOf('user_name')
	var endpos=text.indexOf('&phone')
	user_name=text.substring(startpos+'user_name='.length,endpos);
	startpos=text.indexOf('address=')
	endpos=text.indexOf('&sex')
	address=text.substring(startpos+'address='.length,endpos)
	startpos=text.indexOf('phone=')
	endpos=text.indexOf('&address')
	phone=text.substring(startpos+'phone='.length,endpos)
	prices=$('.price')
	totalprice=0;
	var len=prices.length
	for(var i=0; i < len;i++){
		var temp=prices[i];
		totalprice=totalprice+parseFloat(temp.innerHTML)
	}
	$('#back').click(function(){
		
		window.location.href='/?user_name='+user_name;
	})
	$('#step_pay').click(function(){
		window.location.href='/check_submit/?name='+user_name+'&address='+address+'&phone='+phone
			+'&totalprice='+totalprice;
	})
	
})

