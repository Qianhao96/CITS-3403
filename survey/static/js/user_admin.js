/*jslint browser: true*/
/*global $, jQuery, alert*/
$(document).ready(function () {
	$('.a_d_u').on('click', function(){
    	$(this).parent().parent().addClass('selected');
    });

	userInitialization();
	categoryInitialization();
	pollInitialization();
	responseInitialization();
});

function userInitialization() {
	var user_table = $('#user_table').DataTable();

    ajaxDeletion(user_table, '#cancel_delete_user', '#admin_delete_user', '/admin_delete_user')
}

function categoryInitialization() {
	var category_table = $('#category_table').DataTable();

    ajaxDeletion(category_table, '#cancel_delete_category', '#admin_delete_category', '/admin_delete_category')
}

function pollInitialization(){
	var poll_table = $('#poll_table').DataTable();

 	ajaxDeletion(poll_table, '#cancel_delete_poll', '#admin_delete_poll', '/admin_delete_poll')
}

function responseInitialization(){
	var response_table = $('#response_table').DataTable();

	ajaxDeletion(response_table, '#cancel_delete_response', '#admin_delete_response', '/admin_delete_response')
}


function ajaxDeletion(table, cancel_delete, admin_delete, url){
	$(cancel_delete).on('click', function(){
    	$('.selected').removeClass('selected');
    });

    $(admin_delete).click(function(){
    	var id = $('.selected').attr('id')
		$.ajax({
			url: url,
			dataType: "json",
			data: JSON.stringify({'id': id}),
			contentType: "application/json; charset=utf-8",
			type: 'POST',
			success: function(response){
				displayMessage(table, response['message'], 'success')
			},
			error: function(error){
				displayMessage(table, response['message'], 'error')
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






