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

	$(".vote").click(function () {
		var $this = this;
		$("#confirmModal").modal();
		$(".agree-btn").click(function () {
			$("#confirmModal").modal('hide');
			send_vote($this);
		});

		$(".dismiss-btn").click(function () {
			$("#confirmModal").modal('hide');
		});
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
			$("#successModal").modal();
		},
		error: function (error) {
			$("#failModal").modal();
		}
	});
}
