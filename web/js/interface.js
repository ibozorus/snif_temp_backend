$(document).ready(function () {
    var myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");

    let requestOptionsSensorAlle = {
        method: 'GET',
        redirect: 'follow'
    };
    fetch("http://localhost:8080/sensor/all", requestOptionsSensorAlle)
        .then(response => {
            response.json().then(result => {
                for (let i = 0; i < result.length; i++) {
                    let optionText = "Sensor " + result[i].id;
                    let optionValue = "sensor-" + result[i].id;
                    $('#sensor-select').append(`<option value="${optionValue}"> 
                                       ${optionText} 
                                  </option>`);
                }
            })
        })
        .catch(error => console.log('error', error));
})