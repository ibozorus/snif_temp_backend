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

    function getLast10Temp() {
        $("#lastEntries").empty();
        let requestOptionsLast10 = {
            method: 'GET',
            headers: myHeaders,
            redirect: 'follow'
        };
        let value = $('#sensor-select').val();
        let sensorId = value.split('-')[1];
        fetch("http://localhost:8080/temperature/getLastTemp/" + sensorId, requestOptionsLast10)
            .then(response => {
                response.json().then(result => {
                    for (let i = 0; i < result.length; i++) {
                        let tempValue = result[i];
                        $("#lastEntries").append(`<li> 
                                       ${tempValue} 
                                  </li>`)
                    }
                })
            })
            .then(result => console.log(result))
            .catch(error => console.log('error', error));
    }

    function changeSelect() {
        getLast10Temp();
        $("#average").val("")
        $("#maxMessuredTemp").val("");
        $("#maxTemp").val("");
        let value = $('#sensor-select').val();
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
                    $("#maxMessuredTemp").val(maxtemp);
                    let festgelegteMax = result[0].sensor.maxTemp
                    $("#maxTemp").val(festgelegteMax);
                })
            })
            .catch(error => console.log('error', error));
        loadChart();
    }


    function loadChart() {
        console.log("chart is initialized!");
        const xValues = [];
        const    yValues = [];
        let requestOptionsCharts = {
            method: 'GET',
            headers: myHeaders,
            redirect: 'follow'
        };
        let value = $('#sensor-select').val();
        let sensorId = value.split('-')[1];
        fetch("http://localhost:8080/temperature/" + sensorId, requestOptionsCharts)
            .then(response => {
                response.json().then(result => {
                    for (let i = 0; i < result.length; i++) {
                        let date = new Date(result[i].timestamp);
                        xValues.push(date.toISOString().split("T")[0]);
                        yValues.push(result[i].value);
                    }
                })
            })
            .then(result => console.log(result))
            .catch(error => console.log('error', error));
        console.log(xValues)
        console.log(yValues)
        new Chart("myChart", {
            type: "line",
            data: {
                labels: xValues,
                datasets: [{
                    fill: true,
                    lineTension: 0,
                    backgroundColor: "rgba(0,0,255,1.0)",
                    borderColor: "rgba(0,0,255,0.1)",
                    data: yValues
                }]
            },
            options: {
                legend: {display: false},
                scales: {
                    yAxes: [{ticks: {min: 0.00, max: 100.00}}],
                }
            }
        });
    }
})