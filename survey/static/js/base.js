var dw_id = ["about", "Deve", "ur-info"]

$(document).ready(function () {
	setInterval(function () {
		dateTime()
	}, 500);

	//	$(".click-dropsown").click(function () {
	//		var ids = $(this).attr("id");
	//		for (var i = 0; i < 3; i++) {
	//			if (dw_id[i] != ids) $("." + dw_id[i]).hide();
	//		}
	//		$("." + ids).show("slow");
	//	});

	$(".click-dropsown").each(function () {
		var $this = this;
		var clicked = false;
		$($this).click(function () {
			if(clicked==false){
				$("." + $($this).attr("id")).show("slow");
				clicked=true;
			}
			else $("." + $($this).attr("id")).hide("slow");
		});
	});
});

function dateTime() {
	var today = new Date();
	var date = today.getFullYear() + '-' + (today.getMonth() + 1) + '-' + today.getDate();
	var time = today.getHours() + ":" + today.getMinutes() + ":" + today.getSeconds();
	var dateTime = date + ' ' + time;
	$('#current_time').html(dateTime);
}
