function delete_response(param) {
	var id = $(param).attr('id');
	$.ajax({
		url: "/delete_response",
		dataType: "json",
		data: JSON.stringify({
			'rm_poll_id': id
		}),
		contentType: "application/json; charset=utf-8",
		type: 'POST',
		success: function (response) {
			alert(response['message'])
			window.location.reload(true);
		},
		error: function (error) {
			alert(response['message'])
		}
	});
}

$(document).ready(function () {
	$(".rm-vote").click(function () {
		delete_response(this);
	});
});
