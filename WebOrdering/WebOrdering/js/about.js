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
		window.location.href='/check_phone';
	})

	$('#home').click(function(){
		window.location.href='/';
	})
	
})

function showSection (id) {
	var sections = document.getElementsByTagNames("sections");
	for (var i=0;i<sections.length;i++){
		if (sections[i].getAttribute("id") != id){
		sections[i].style.dispaly = "none";
	    }else{
		sections[i].style.dispaly = "block";
	    }
    }
}