function phoneAdd()
{

}

function addressAdd()
{

}

function chooseCollapse()
{
	var a = document.getElementById("span_1");
	var b = document.getElementById("in_5");
	var c = document.getElementById("btn_1");
	a.style.visibility = "collapse";	
	b.style.visibility = "collapse";
	c.style.visibility = "collapse";
}
function chooseCollapse_2()
{
	var a = document.getElementById("span_2");
	var b = document.getElementById("in_6");
	var c = document.getElementById("btn_2");
	a.style.visibility = "collapse";	
	b.style.visibility = "collapse";
	c.style.visibility = "collapse";
}
function phoneShow_new()
{
	var a = document.getElementById("span_1");
	var b = document.getElementById("in_5");
	var c = document.getElementById("btn_1");
	var d = document.getElementById("in_1")
	a.style.visibility = "visible";	
	b.style.visibility = "visible";
	c.style.visibility = "visible";
	d.checked = false;
}

function blurShow(b)
{
	var a = document.getElementById(b);
	if(a.value == "")
	{
		a.value = "请输入";
	}
	a.style.color = "gray"
}


function focusHide(b)
{
	var a = document.getElementById(b);
	if(a.value == "请输入")
	{
		a.value = "";
	}
	a.style.color = "black";

}

function phoneShow_old()
{
	var a = document.getElementById("span_1");
	var b = document.getElementById("in_5");
	var c = document.getElementById("btn_1");
	var d = document.getElementById("in_7")
	a.style.visibility = "visible";	
	b.style.visibility = "visible";
	c.style.visibility = "visible";
	d.checked = false;
}

function phoneShow_old_2()
{
	var a = document.getElementById("span_2");
	var b = document.getElementById("in_6");
	var c = document.getElementById("btn_2");
	var d = document.getElementById("in_7")
	a.style.visibility = "visible";	
	b.style.visibility = "visible";
	c.style.visibility = "visible";
	d.checked = false;
}


