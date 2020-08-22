Chart.defaults.global.defaultFontFamily = 'Nunito', '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#858796';

var endpoint = '/iot_app/api/TempViewSet/';
//var defaultData = [];
//var labels = [];
$.ajax({
  method: "GET",
  url: endpoint,
  success: function(data){
    console.log(data)
    labels = data.labels
    defaultData = data.default
    setChart();
},
  error: function(error_data){
    console.log("error")
    console.log(error_data)
  }
})

// function setChart(){
//   var ctx = document.getElementById('myTemperatureChart').getContext('2d');
//   var myTemperatureChart = new Chart(ctx, {
//     type: 'bar',
//     data: {
//       labels: labels,
//       datasets: [{
//         label: '# no of votes',
//         data: data.default,
//       }]
//     }
//   })
// }


function DayChartTemp() {
    $.ajax({
        method: "GET",
        url: '/iot_app/api/DayChartTemp/',
        success: function (data) {
            console.log(data)
            labels = data.labels
            defaultData = data.default
            setChart()
        },
        error: function (error_data) {
            console.log("error")
            console.log(error_data)
        }
    })

};
function WeekChartTemp() {
    $.ajax({
        method: "GET",
        url: '/iot_app/api/WeekChartTemp/',
        success: function (data) {
            console.log(data)
            labels = data.labels
            defaultData = data.default
            setChart()
        },
        error: function (error_data) {
            console.log("error")
            console.log(error_data)
        }
    })

};
function MonthChartTemp() {
    $.ajax({
        method: "GET",
        url: '/iot_app/api/MonthChartTemp/',
        success: function (data) {
            console.log(data)
            labels = data.labels
            defaultData = data.default
            setChart()
        },
        error: function (error_data) {
            console.log("error")
            console.log(error_data)
        }
    })

};
function YearChartTemp() {
    $.ajax({
        method: "GET",
        url: '/iot_app/api/YearChartTemp/',
        success: function (data) {
            console.log(data)
            labels = data.labels
            defaultData = data.default
            setChart()
        },
        error: function (error_data) {
            console.log("error")
            console.log(error_data)
        }
    })

};

//  < canvas id = "myChart" width = "400" height = "400" ></canvas >
//<script>
function setChart(){
var ctx = document.getElementById('myTemperatureChart');
var myTemperatureChart = new Chart(ctx, {
        type: 'line',
    data: {
        labels: labels,
        datasets: [{
            label: 'Temp',
            fill: false,
            data: defaultData,
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: {
        scales: {
        yAxes: [{
        ticks: {
        //beginAtZero: false
        //min: 0
            max: 40,
            min: 10,
            stepSize: 10,
            maxTicksLimit: 4,
            // Include a Degree Celcius sign in the ticks
            callback: function (value, index, values) {
                return value + '°C';
                }
                },
            gridLines: {
                color: "rgb(234, 236, 244)",
                zeroLineColor: "rgb(234, 236, 244)",
                drawBorder: false,
                borderDash: [2],
                zeroLineBorderDash: [2]
            }
            }],
        xAxes: [{
            display: false
            //time: {
            //     unit: 'time',
            //     parser: 'HH:MM:SS',
            //     //tooltipFormat: 'll HH:mm',
            //     unitStepSize: 1,
            //     displayFormats: {
            //         'time': 'HH:MM:SS'
            //     }
            // },
            // ticks: {
            //     maxTicksLimit: 4
            // },
            // gridLines: {
            //     display: false,
            //     drawBorder: false
            //}
        }]
        },
        legend: {
            display: false
        },
        // tooltips: {
        //     backgroundColor: "rgb(255,255,255)",
        //     bodyFontColor: "#858796",
        //     titleMarginBottom: 10,
        //     titleFontColor: '#6e707e',
        //     titleFontSize: 14,
        //     borderColor: '#dddfeb',
        //     borderWidth: 1,
        //     xPadding: 15,
        //     yPadding: 15,
        //     displayColors: false,
        //     intersect: false,
        //     mode: 'index',
        //     caretPadding: 10
        //     // callbacks: {
        //     //     label: function (tooltipItem, chart) {
        //     //         var datasetLabel = chart.datasets[tooltipItem.datasetIndex].label || '';
        //     //         return datasetLabel + '$' ;
        //     //     }
        //     // }
        // }        
    }
});

}


