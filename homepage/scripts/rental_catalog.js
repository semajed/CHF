$(function(){

	$('#shopping_cart_modal').modal({
        show: false,
    });//initialize modal

    $('.add_button').on('click',function(){
        var pid = $(this).attr('data-pid');
        var qty = 1;
        $('#shopping_cart_modal').modal('show');
        $.ajax({
        	url: '/homepage/rental_cart.add/' + pid + "/" + qty,
        	success: function(data){
        		$('#shopping_cart_modal').find('.shopping_cart_contents').html(data)
        	},//success
        });//ajax
    });//add_button click

    $('.view_button').on('click',function(){
    	var qty = 1;
        $('#shopping_cart_modal').modal('show');
        $.ajax({
        	url: '/homepage/rental_cart/' + qty,
        	success: function(data){
        		$('#shopping_cart_modal').find('.shopping_cart_contents').html(data)
        	},//success
        });//ajax
    });//add_button click

    $('#searchBar').on('keyup', function(){

    	var searchBarParams = $('#searchBar').val().toLowerCase();

    	$(".box").each(function(){
    		var item = $(this).find('#pname').text();
    		if (item.toLowerCase().indexOf(searchBarParams) === -1){
    			$(this).hide();
    		}else{
    			$(this).show();
    		}//end if

    // 		if(searchBarParams != item){
				// $.ajax({
		  //       	url: '/homepage/searchResults/',
		  //       	success: function(data){
		  //       		$('#productList').html(data)
		  //       	},//success
		  //       });//ajax
    // 		};

    	});//box each

    });//search bar





});