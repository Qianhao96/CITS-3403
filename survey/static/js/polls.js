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
})
