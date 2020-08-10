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
var endpoint = '/TempViewSet/'
var defaultData = []
var labels = []
$.ajax({
  method: "GET",
  url: endpoint,
  success: function(data){
    console.log(data)
    labels = data.labels
    defaultData = data.default
    setChart()
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
            label: 'Temperature Details',
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
            max: 55,
            min: 5,
            stepSize: 5 
                }
            }]
        }
    }
});
}
//</script>