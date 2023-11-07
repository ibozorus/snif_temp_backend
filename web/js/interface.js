$(document).ready(function () {

    $("#select-button").on("click", changeSelect)

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

    function changeSelect() {
        let value = $('#sensor-select').val();
        console.log(value);
        let sensorId = value.split('-')[1];
        var requestOptionsAvg = {
            method: 'GET',
            headers: myHeaders,
            redirect: 'follow'
        };
        fetch("http://localhost:8080/temperature/getAvgTemp/" + sensorId, requestOptionsAvg)
            .then(response => {
                response.json().then(result => {
                    let avgTemp = result[0];
                    $("#average").val(avgTemp);
                })
            })
            .catch(error => console.log('error', error));
        fetch("http://localhost:8080/temperature/getMaxTemp/" + sensorId, requestOptionsAvg)
            .then(response => {
                response.json().then(result => {
                    let maxtemp = result[0].value;
                    console.log(result[0])
                    $("#maxMessuredTemp").val(maxtemp);
                    let festgelegteMax = result[0].sensor.maxTemp
                    $("#maxTemp").val(festgelegteMax);
                })
            })
            .catch(error => console.log('error', error));
    }
})