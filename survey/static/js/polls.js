$(document).ready(function () {
	var swiper = new Swiper('.swiper-container', {
		spaceBetween: 130,
		pagination: {
			el: '.swiper-pagination',
			type: 'progressbar',
		},
		navigation: {
			nextEl: '.swiper-button-next',
			prevEl: '.swiper-button-prev',
		},
	});

	$(".vote").click(function() {
		send_vote(this);
	});
})

function send_vote(param) {
	var id = $(param).attr('id');
	$.ajax({
		url: "/vote",
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
