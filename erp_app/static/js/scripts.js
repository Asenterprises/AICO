$(document).ready(function() {
    // Login form submission
    $('#login-form').submit(function(e) {
        e.preventDefault();
        $.ajax({
            type: 'POST',
            url: '/login',
            data: $(this).serialize(),
            success: function(response) {
                if (response.message === 'login_success') {
                    window.location.href = '/dashboard';
                } else {
                    alert('Login failed. Please try again.');
                }
            }
        });
    });

    // Registration form submission
    $('#register-form').submit(function(e) {
        e.preventDefault();
        $.ajax({
            type: 'POST',
            url: '/register',
            data: $(this).serialize(),
            success: function(response) {
                if (response.message === 'registration_success') {
                    window.location.href = '/login';
                } else {
                    alert('Registration failed. Please try again.');
                }
            }
        });
    });

    // Noodle manufacturing process form submission
    $('#noodle-process-form').submit(function(e) {
        e.preventDefault();
        $.ajax({
            type: 'POST',
            url: '/start_process',
            data: $(this).serialize(),
            success: function(response) {
                if (response.message === 'process_start') {
                    alert('Noodle manufacturing process started.');
                } else {
                    alert('Process start failed. Please try again.');
                }
            }
        });
    });

    // End process button click
    $('#end-process-button').click(function() {
        $.ajax({
            type: 'POST',
            url: '/end_process',
            success: function(response) {
                if (response.message === 'process_end') {
                    alert('Noodle manufacturing process ended.');
                } else {
                    alert('Process end failed. Please try again.');
                }
            }
        });
    });
});