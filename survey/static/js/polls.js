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
		var element = $("#card-img").css("height");
		console.log(element);
		$("#confirmModal").modal();
		$(".agree-btn").click(function () {
			$("#confirmModal").modal('hide');
			send_vote($this);
		});

		$(".dismiss-btn").click(function () {
			$("#confirmModal").modal('hide');
		});
	});
	//    var style = window.getComputedStyle(element);
	//    var height = style.getPropertyValue('height');
	//	console.log(height);
	//	$(".poll-describe").css("height:" +height);

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
			$(".success-btn").click(function () {
				window.location.reload(true);
			});
		},
		error: function (error) {
			$("#failModal").modal();
			$(".failure-btn").click(function () {
				window.location.href = "/";
			});
		}
	});
}
