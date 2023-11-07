$(document).ready(function () {
    var settings = {
        "url": "localhost:8080/user/check-login",
        "method": "GET",
        "timeout": 0,
        "headers": {
            "Content-Type": "application/json"
        },
        "data": JSON.stringify({
            "username": "scott31",
            "password": "12345"
        }),
    };

    $.ajax(settings).done(function (response) {
        console.log(response);
    });
    $("#login-button").on("click", function () {
        let username = $("#username").val();
        let password = $("#password").val();

    })

})