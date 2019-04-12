function mouse_enter(pram) {
	$(pram).find(".submenu").show();
}

function mouse_leave(pram){
	var $this = $(this);
	$(pram).find(".submenu").hide(2000);
}

$((document)).ready(function () {
	$(".submenu").hide();
	$(".item").mouseenter(function () {
		mouse_enter(this);
	});

	$(".item").mouseleave(function () {
		mouse_leave(this);
	});


});
