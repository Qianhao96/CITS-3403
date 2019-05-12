var trans_change = 0;
$(document).ready(function () {
	setInterval(function () {
		transperenty()
	}, 1000);

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

	$(".youtube").click(function () {
		var modalHref = $(this).attr("href");
		var youtubeHref = $(this).children("img").attr("id");
		if ($(modalHref).children().length == 0) {
			$(modalHref).append("<div class='modal-dialog'><div class='modal-content' style='background-color: black; padding=0px;'><div class='modal-body'><iframe class='video-frame' style='width:100%; height: 300px;' src=" + youtubeHref + " frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen</iframe></div></div></div>");
		}
	});
});

function transperenty() {
	trans_change += 0.1;
	trans_change = trans_change % 1.0;
	console.log(trans_change);
	$(".press").css("opacity",""+trans_change);
}

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
