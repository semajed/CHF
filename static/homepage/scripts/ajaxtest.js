$(function(){

	$('#id_username').on('change',function(){

		var username = $('#id_username').val();

		$.ajax({
			url: '/homepage/ajaxtest.check_username/',
			data: {
				u: username,
			},
			type: "POST",
			success: function(resp){
				if (resp == '1'){
					$('#id_username_message').text('this username looks great');
				}else{
					alert("terrible");
				}//if
			},//success
		});//ajax

	});//change


});//ready