$(function(){
    // bind 'myForm' and provide a simple callback function
    $('#login_form').ajaxForm(function(data) {
        $("#jquery-loadmodal-js-body").html(data);
    });//ajax form
});