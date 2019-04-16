/*jslint browser: true*/
/*global $, jQuery, alert*/
$(document).ready(function () {
    var user_table = $('#user_table').DataTable();

    $('.a_d_u').on('click', function(){
    	$(this).parent().parent().addClass('selected');
    });

    $('#cancel_delete_user').on('click', function(){
    	$('.selected').removeClass('selected');
    });

    $('#admin_delete_user').click(function(){
    	var email = $('.selected').attr('value')
		$.ajax({
			url: '/admin_delete_user',
			dataType: "json",
			data: JSON.stringify({'email': email}),
			contentType: "application/json; charset=utf-8",
			type: 'POST',
			success: function(response){
				user_table.row('.selected').remove().draw( false );
				$('#js_alert_message').addClass('alert alert-success');
				$('#js_alert_message').css('text-align', 'center');
				$('#js_alert_message').html(response['message']);
			},
			error: function(error){
				$('#js_alert_message').addClass('alert alert-danger');
				$('#js_alert_message').css('text-align', 'center');
				$('#js_alert_message').html('Deteltion failed, please refresh the page to try again');
			}
		});
    });
});
