$(document).ready(function(){
    $('#registerForm').on('submit', function(e){
        e.preventDefault();
        let err = 0;
        if ($('#fullname').val().trim() === '' || $('#password').val().trim() != $('#confirm_password').val().trim()){
            err = 1;
        }
        if (err == 0){
            $.ajax({
                url: '/user_register',
                method: 'POST',
                contentType: 'application/json',
                data: JSON.stringify({
                    name: $('#fullname').val(),
                    password: $('#password').val(),
                    email: $('#email').val()
                })
            }).done(function(data){
                if(data.result){
                    window.location.href = '/login';
                }else{
                    alert('on loh');
                }
            });
        } 
    });

    $('#loginForm').on('submit', function(e){
        e.preventDefault();
        $.ajax({
            url: '/user_login',
            method: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({
                username: $('#username').val(),  
                password: $('#password').val()
            })
        }).done(function(data){
            if(data.result){
                window.location.href = '/dashboard';
            }else{
                alert('on loh');
            }
        })
    });
});