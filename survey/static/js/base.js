$(document).ready(function () {
	setInterval(function() {
  		dateTime()
	}, 500);
});

function dateTime(){
	var today = new Date();
	var date = today.getFullYear()+'-'+(today.getMonth()+1)+'-'+today.getDate();
	var time = today.getHours() + ":" + today.getMinutes() + ":" + today.getSeconds();
	var dateTime = date+' '+time;
	$('#current_time').html(dateTime);
}
