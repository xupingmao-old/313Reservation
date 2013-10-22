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
	var sections = document.getElementsByTagName("sections");
	for (var i=0;i<sections.length;i++){
		if (sections[i].getAttribute("id") != id){
		sections[i].style.dispaly = "none";
	    }else{
		sections[i].style.dispaly = "block";
	    }
    }
}

function prepareInternalnav () {
	if (!document.getElementsByTagName) return false;
	if (!document.getElementById) return false;
	var articles = document.getElementsByTagName("article");
	if (articles.length == 0) return false;
	var navs = articles[0].getElementsByTagNames("nav");
	if (navs.length == 0) return false;
	var nav = navs[0];
	var links = nav.getElementsByTagName("a");
	for (var i=0;i<links.length;i++){
		var sectionId = links[i].getAttribute("href").split("#")[1];
	    if (!document.getElementById(sectionId)) continue;
	    document.getElementById(sectionId).style.dispaly = "none";
	    links[i].destination = sectionId;
	    links[i].onclick = function(){
	    	showSection(this.destination);
	    	return false;
	    }
	}    
}

function addLoadEvent(func){
	var oldonload = window.onload;
	if (typeof window.onload != 'function'){
		window.onload = func;
	}else{
		window.onload = function(){
			oldonload();
			func();
		}
	}
}

addLoadEvent(prepareInternalnav);