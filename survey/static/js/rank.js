function getRandomColor() {
	var letters = '0123456789ABCDEF';
	var color = '#';
	for (var i = 0; i < 6; i++) {
		color += letters[Math.floor(Math.random() * 16)];
	}
	return color;
}


function gerListRandomColor(length) {
	var colors = new Array(length);
	for (var i = 0; i < length; ++i) {
		colors[i] = getRandomColor();
	}
	return colors;
}

function displaybarChart(param) {
	var id = $(param).attr('name');
	$.ajax({
		url: "/getOverview",
		dataType: "json",
		data: JSON.stringify({
			'id': id
		}),
		contentType: "application/json; charset=utf-8",
		type: 'POST',
		success: function (message) {
			if ((message.data[0]).length > 0 && (message.data[1]).length > 0){
				$("#bar-chart"+id).show();
				$("#line-chart"+id).hide();
				new Chart(document.getElementById("bar-chart"+id), {
					type: 'horizontalBar',
					data: {
						labels: message.data[0],
						datasets: [{
							label: "Votes",
							backgroundColor: gerListRandomColor(5),
							data: message.data[1]
					}]
					},
					options: {
						legend: {
							display: false
						},
						scales: {
							xAxes: [{
								ticks: {
									suggestedMin: 0,
									suggestedMax: message.data[1][0] + 1
								}
	            			}]
						}
					}
				});
			}else{
				$('#info'+id).html('There is no value to display');
				$('#poll-button'+id).hide()
			}
		}
	});
}

function data(dict) {
	arr = new Array();
	for (var key in dict) {
		var temp = {
			data: dict[key],
			label: key,
			borderColor: getRandomColor(),
			fill: false
		}
		arr.push(temp);
	}
	return arr;
}

function displaylineChart(param) {
	var id = $(param).attr('name');
	$.ajax({
		url: "/getElaborate",
		dataType: "json",
		data: JSON.stringify({
			'id': id
		}),
		contentType: "application/json; charset=utf-8",
		type: 'POST',
		success: function (response) {
			$("#bar-chart"+id).hide();
			$("#line-chart"+id ).show();
			new Chart(document.getElementById("line-chart"+id), {
				type: 'line',
				data: {
					labels: response.label,
					datasets: data(response.data)
				}
			});
		}
	});
}

$(document).ready(function () {
	$(".overview").each(function(index) {
		displaybarChart(this);
	});

	$(".elaborate").click(function () {
		displaylineChart(this);
	});

	$(".overview").each(function(index) {
		$(this).click(function () {
			displaybarChart(this);
		});
	});

});
