/*jslint browser: true*/
/*global $, jQuery, alert*/
$(document).ready(function () {
	$('.a_d_u').on('click', function(){
    	$(this).parent().parent().addClass('selected');
    });

	userInitialization();
	categoryInitialization();
});

function userInitialization() {
	var user_table = $('#user_table').DataTable();

    $('#cancel_delete_user').on('click', function(){
    	$('.selected').removeClass('selected');
    });

    $('#admin_delete_user').click(function(){
    	var email = $('.selected').attr('id')
		$.ajax({
			url: '/admin_delete_user',
			dataType: "json",
			data: JSON.stringify({'email': email}),
			contentType: "application/json; charset=utf-8",
			type: 'POST',
			success: function(response){
				displayMessage(user_table, response['message'], 'success')
			},
			error: function(error){
				displayMessage(user_table, response['message'], 'error')
			}
		});
    });
}

function categoryInitialization(argument) {
	var response_table = $('#response_table').DataTable();

	$('#cancel_delete_category').on('click', function(){
    	$('.selected').removeClass('selected');
    });

    $('#admin_delete_category').click(function(){
    	var id = $('.selected').attr('id')
		$.ajax({
			url: '/admin_delete_category',
			dataType: "json",
			data: JSON.stringify({'id': id}),
			contentType: "application/json; charset=utf-8",
			type: 'POST',
			success: function(response){
				displayMessage(response_table, response['message'], 'success')
			},
			error: function(error){
				displayMessage(response_table, response['message'], 'error')
			}
		});
    });
}


function displayMessage(table, message, type) {
	if(type.localeCompare('success') == 0){
		table.row('.selected').remove().draw( false );
		$('#js_alert_message').addClass('alert alert-success');
		$('#js_alert_message').css('text-align', 'center');
		$('#js_alert_message').html(message);
	}
	else{
		$('#js_alert_message').addClass('alert alert-danger');
		$('#js_alert_message').css('text-align', 'center');
		$('#js_alert_message').html('Deteltion failed, please refresh the page and try again');
	}
}