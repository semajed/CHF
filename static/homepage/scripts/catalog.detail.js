$(function(){

    $('.add_button').on('click',function(){
        console.log($(this));
        var pid = $(this).attr('data-pid');
        var qty = $(this).attr('data-qty');
        $('#shopping_cart_modal').modal('show');
        $.ajax({
        	url: '/homepage/shopping_cart.add/' + pid + "/" + qty,
        	success: function(data){
        		$('#shopping_cart_modal').find('.shopping_cart_contents').html(data)
        	},//success
        });//ajax
    });//add_button click

    $('.view_button').on('click',function(){
        var qty = 1;
        $('#shopping_cart_modal').modal('show');
        $.ajax({
            url: '/homepage/shopping_cart/' + qty,
            success: function(data){
                $('#shopping_cart_modal').find('.shopping_cart_contents').html(data)
            },//success
        });//ajax
    });//add_button click

});//ready