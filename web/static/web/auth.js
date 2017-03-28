$(document).ready(function() {
    $('#login-form').submit(function(event) {
        event.preventDefault();
        var data = $(this).serializeArray().reduce(function(result, val) {
            result[val.name] = val.value;
            return result;
        }, {});

        $.ajax({
            method: 'POST',
            url: '/api/auth/login',
            contentType: 'application/json',
            data: JSON.stringify(data),
            success: function() {
                location.reload();
            },
            error: function() {
                alert('Unable to login. Please check username and password, and try again');
            }
        });
    });

    $('#sign-out').click(function(){
    	$.ajax({
            method: 'POST',
            url: '/api/auth/logout',
            contentType: 'application/json',
            success: function() {
                location.reload();
            },
            error: function() {
                alert('Unable to logout. Please contact the site administrator');
            }
        });
    });

    $('#signup-form').submit(function(event) {
        event.preventDefault();
        var data = $(this).serializeArray().reduce(function(result, val) {
            result[val.name] = val.value;
            return result;
        }, {});

        $.ajax({
            method: 'POST',
            url: '/api/auth/register',
            contentType: 'application/json',
            data: JSON.stringify(data),
            success: function() {
            	alert('Successfully registered');
            	setTimeout(function(){
            		location.href = "/";
            	}, 1000);
            },
            error: function() {
                alert('Unable to sign up. Please check entered values');
            }
        });
    });
});