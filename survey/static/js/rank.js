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
	var id = $(param).attr('id');
	$.ajax({
		url: "/getOverview",
		dataType: "json",
		data: JSON.stringify({
			'id': id
		}),
		contentType: "application/json; charset=utf-8",
		type: 'POST',
		success: function (message) {
			$("#bar-chart").show();
			$("#line-chart").hide();
			new Chart(document.getElementById("bar-chart"), {
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
								suggestedMax:message.data[1][0]+1
							}
            			}]
					}
				}
			});
		}
	});
}

function displaylineChart(param) {
	$("#bar-chart").hide();
	$("#line-chart").show();
	new Chart(document.getElementById("line-chart"), {
		type: 'line',
		data: {
			labels: ["21/08/2019", "22/08/2019", "23/08/2019", "24/08/2019", "25/08/2019", "26/08/2019", "27/08/2019", "28/08/2019", "29/08/2019", "30/08/2019"],
			datasets: [{
					data: [86, 114, 106, 106, 107, 111, 133, 221, 783, 2478],
					label: "music_5",
					borderColor: "#3e95cd",
					fill: false
			}, {
					data: [282, 350, 411, 502, 635, 809, 947, 1402, 3700, 5267],
					label: "music_4",
					borderColor: "#8e5ea2",
					fill: false
			}, {
					data: [168, 170, 178, 190, 203, 276, 408, 547, 675, 734],
					label: "music_3",
					borderColor: "#3cba9f",
					fill: false
			}, {
					data: [40, 20, 10, 16, 24, 38, 74, 167, 508, 784],
					label: "music_2",
					borderColor: "#e8c3b9",
					fill: false
			}, {
					data: [6, 3, 2, 2, 7, 26, 82, 172, 312, 433],
					label: "music_1",
					borderColor: "#c45850",
					fill: false
      }
    ]
		}
	});
}

function test(param){
	var id = $(param).attr('id');
	$.ajax({
		url: "/getElaborate",
		dataType: "json",
		data: JSON.stringify({
			'id': id
		}),
		contentType: "application/json; charset=utf-8",
		type: 'POST',
		success: function (response) {
			alert(response['message'])
		},
		error: function (error) {
			alert(response['message'])
		}
	});
}

$(document).ready(function () {
	$(".elaborate").click(function () {
		displaylineChart(this);
		test(this);
	});

	$(".overview").click(function () {
		displaybarChart(this);
	});
});
