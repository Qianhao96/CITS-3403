var $items = $('#menu .item');
var cnt_items = $items.length;


function mouse_enter(pram) {
	$(pram).find(".submenu").show();
}

function mouse_leave(pram) {
	var $this = $(this);
	$(pram).find(".submenu").hide(2000);
}

function mouse_leave(pram) {
	$(pram).find(".submenu").hide();
}

function mouse_click_back(pram) {

}

function showContent(idx) {
	var splits = idx.split(" ");
	var x = ".content > " + "." + splits[0];
	console.log(x);
	$(x).show();
	$(".content").stop().animate({
		'left': '2.4%'
	}, 200, function () {
		$(this).find('.' + idx).fadeIn();
	});
}

function mouse_click_about(pram) {
	var $this = $(pram).closest(".item");
	var d = 100;
	var step = 0;

	$(pram).closest(".menu").animate({left: '-18%'});

	$items.not($this).each(function () {
		var $item = $(this);
		$item.stop().animate({
			'marginLeft': '-32%'
		}, d += 200, function () {
			++step;
			if (step == cnt_items - 1) {
				showContent(pram.className);
			}
		});

	});
}


$((document)).ready(function () {
	$(".item").mouseenter(function () {
		mouse_enter(this);
	});

	$(".item").mouseleave(function () {
		mouse_leave(this);
	});

	$(".about").click(function () {
		mouse_click_about(this);
	});

});
