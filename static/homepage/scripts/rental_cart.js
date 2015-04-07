$(function(){

	$('.remove_product').on('click', function(){
		var pid = $(this).attr('data-pid');
        var qty = $(this).attr('data-qty');
		$.ajax({
	       url: '/homepage/rental_cart.remove/' + pid + '/' + qty,
	       success: function(data){
                $('#shopping_cart_modal').find('.shopping_cart_contents').html(data)
        	},//success
        });//ajax
	});//remove_product button click

                //login modal
        $('#login_dialog').modal({
            show: false,
        });//initialize modal

        $('.show_login_dialog').on('click',function(){
            $.loadmodal({
                url: '/homepage/base.loginform/',
                title: 'Login',
                width: '600px',
            });//loadmodal
        });//click
});//ready