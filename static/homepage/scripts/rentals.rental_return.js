$(function($) {
    $('.change_condition').on('change', function(){
        var rid = $(this).attr('data-rid');
        var new_condition = ($(this).val());
        if(new_condition == "-------"){
            return false;
        }
        console.log($(this).val())
        $(this).addClass("success");
        $.ajax({
            url: "/homepage/rentals.change_condition/" + rid + "/" + new_condition + "/",
            success: function(data){
                console.log("SUCCESS");

                // $(this).addClass("success");
                // $('.change_condition').addClass('success');
                // $('#shopping_cart_modal').find('.shopping_cart_contents').html(data)
            },//success
        });//ajax
    });//change condition

    $('.fees').on('change', function(){

        var damage = $('#box1').val();
        var late = $('#box2').val();
        var total = parseFloat(damage) + parseFloat(late);
        var formattedTotal = total.toFixed(2);
        $('#total').val(formattedTotal);

        // var searchBarParams = $('#searchBar').val().toLowerCase();

        // $(".box").each(function(){
        //     var item = $(this).find('#pname').text();
        //     if (item.toLowerCase().indexOf(searchBarParams) === -1){
        //         $(this).hide();
        //     }else{
        //         $(this).show();
        //     }//end if

        // });//box each

    });//search bar
});