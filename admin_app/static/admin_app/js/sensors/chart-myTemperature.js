// var ctx = document.getElementById('myTemperatureChart');

// var stars = [135850, 52122, 148825, 16939, 9763];
// var frameworks = ['React', 'Angular', 'Vue', 'Hyperapp', 'Omi'];

// var myTemperatureChart = new Chart(ctx, {
//   type: 'line',
//   data: {
//     labels: frameworks,
//     datasets: [{
//       label: 'Temperature Data',
//       data: stars
//     }]
//   },
// })

var endpoint = '/TempViewSet/';
var defaultData = [];
var labels = [];
$.ajax({
  method: "GET",
  url: endpoint,
  success: function(data){
    console.log(data)
    labels = data.labels
    defaultData = data.default
    setChart();
    DayChart();
   // myFunction()


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


//  < canvas id = "myChart" width = "400" height = "400" ></canvas >
//<script>
function setChart(){
var ctx = document.getElementById('myTemperatureChart');
var myTemperatureChart = new Chart(ctx, {
        type: 'line',
    data: {
        labels: labels,
        datasets: [{
            label: 'temperature',
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
            maxTicksLimit: 4
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
        }
    }
});

}
//</script>

// function DayChart() {
//     myTemperatureChart.data.labels = labels;
//     //myTemperatureChart.data.datasets[0].data = [1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10,1,2,3,4];
//     // chart.data.datasets[0].data = defaultData;
//     //chart.data.datasets[0].labels = labels;
//     myTemperatureChart.update();
// };
function DayChart() {

    //make an ajax call and get status value using the same 'id'
    //var var1 = document.getElementById("status").value;
    $.ajax({
        method: "GET",
        url: endpoint,
        success: function (data) {
            console.log(data)
            labels = data.labels
            defaultData = data.default
            setChart();
            //DayChart();
            // myFunction()


        },
        error: function (error_data) {
            console.log("error")
            console.log(error_data)
        }
    })

};
