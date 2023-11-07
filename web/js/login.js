$(document).ready(function () {
    var myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");


    $("#login-button").on("click", function () {

        let requestOptions = {
            method: 'POST',
            headers: myHeaders,
            redirect: 'follow'
        };
        let username = $("#username").val();
        let password = $("#password").val();
        let data = {
            username: username,
            password: password
        }
        requestOptions["body"] = JSON.stringify(data);

        fetch("http://localhost:8080/user/check-login", requestOptions)
            .then(response => response.text())
            .then(result => {
                let resultJSON = JSON.parse(result);
                console.log(resultJSON)
                if (resultJSON.message === "success") {
                    window.location.replace("interface.html");
                } else {
                    alert("Fehler beim Einloggen!")
                }

            })
            .catch(error => console.log('error', error));
    })

})