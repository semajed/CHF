$(function(){

    //login modal
    $('#login_dialog').modal({
        show: false,
    });//initialize modal

    $('#show_login_dialog').on('click',function(){
        $.loadmodal({
            url: '/homepage/base.loginform/',
            title: 'Login',
            width: '600px',
        });//loadmodal
    });//click

});