$(function($) {
    $('.change_condition').on('change', function(){
        var rid = $(this).attr('data-rid');
        var new_condition = ($(this).val());
        if(new_condition == "-------"){
            return false;
        }
        console.log($(this).val())
        // $(this).addClass("success");
        $.ajax({
            url: "/homepage/rentals.change_condition/" + rid + "/" + new_condition + "/",
            success: function(data){
                console.log("SUCCESS");
                console.log($(this));
                // $(this).addClass("success");
                $('.change_condition').addClass('success');
                // $('#shopping_cart_modal').find('.shopping_cart_contents').html(data)
            },//success
        });//ajax
    });
});