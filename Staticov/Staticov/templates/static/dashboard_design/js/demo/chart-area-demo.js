// Set new default font family and font color to mimic Bootstrap's default styling
//Chart.defaults.global.defaultFontFamily = 'Nunito', '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
var CITY_INDEX = 3;
var DATE_INDEX = 4;

var COLORS = ["#3e95cd", "#8e5ea2", "#3cba9f"];
var MONTHS = {
  "01": "ינואר",
  "02": "פברואר",
  "03": "מרץ",
  "04": "אפריל",
  "05": "מאי",
  "06": "יוני",
  "07": "יולי",
  "08": "אוגוסט",
  "09": "ספטמבר",
  "10": "אוקטובר",
  "11": "נובמבר",
  "12": "דצמבר",

}

/**
 * 
 * @param {*} dateString - date string in the format: "YYYY-MM-DD"
 * returns date string in the format: "YYYY-MM"
 */
function getDateByMonthAndYear(dateString) {
  return dateString.substring(0, 7);
}

var charData=null;

function handleData(data){
  const data2020 = data.filter((entry) => entry[DATE_INDEX].includes(2020));

  const groupedDataByCity = _.groupBy(
    data,
    entry => getDateByMonthAndYear(entry[CITY_INDEX])
  );
 /// console.log(JSON.stringify(groupedDataByCity));
  const labels = Object.values(MONTHS);
  const datasets = Object.keys(groupedDataByCity).map((entryKey, index) => {
    const entry = groupedDataByCity[entryKey];
    //console.log(JSON.stringify(entry))
    var patientsPerMonths = entry.reduce((acc,next) => {
      var month = next[4].split('-')[1]
      acc[month] = (acc[month] || 0 ) + 1
      return acc
      },{ '01':0,'02':0,'03':0,'04':0,'05':0,'06':0,'07':0,'08':0,'09':0,'10':0,'11':0,'12':0}
      )    
      //console.log(entryKey)
    return {
          data: Object.values(patientsPerMonths),
          label: entryKey,
          borderColor: COLORS[index % COLORS.length],
          fill: false
    }
  })
  //  [ID, Taz,       Age,  City,  Date,        Religion]
  //  [1, "743119585", 103, "BA", "2020-08-28", "HA"]
  // TODO: group data by months which will be used as the labels
  new Chart(document.getElementById("line-chart"), {
    type: 'line',
    data: {
      labels,
      datasets
    },
    options: {
      title: {
        display: true,
        text: 'מספר נדבקים לעיר'
      }
    }
  });
}

function handleError(error){
  console.log({error});
}

$.ajax({url:"http://localhost:8000/Staticov/datapatient", success: handleData, error: handleError});


// new Chart(document.getElementById("line-chart"), {
//   type: 'line',
//   data: {
//     labels: [1,5,10,20,30,40,60,80,100,120],
//     datasets: [{ 
//         data: [86,114,106,106,107,111,133,221,783,2478],
//         label: "באר שבע",
//         borderColor: "#3e95cd",
//         fill: false
//       }, { 
//         data: [282,350,411,502,635,809,947,1402,3700,5267],
//         label: "תל אביב",
//         borderColor: "#8e5ea2",
//         fill: false
//       }, { 
//         data: [168,170,178,190,203,276,408,547,675,734],
//         label: "אילת",
//         borderColor: "#3cba9f",
//         fill: false
//       }, { 
//         data: [40,20,10,16,24,38,74,167,508,784],
//         label: "חיפה",
//         borderColor: "#e8c3b9",
//         fill: false
//       }, { 
//         data: [6,3,2,2,7,26,82,172,312,433],
//         label: "ירושלים",
//         borderColor: "#c45850",
//         fill: false
//       }
//     ]
//   },
//   options: {
//     title: {
//       display: true,
//       text: 'מספר נדבקים לעיר'
//     }
//   }
// });

/*
function number_format(number, decimals, dec_point, thousands_sep) {
  // *     example: number_format(1234.56, 2, ',', ' ');
  // *     return: '1 234,56'
  number = (number + '').replace(',', '').replace(' ', '');
  var n = !isFinite(+number) ? 0 : +number,
    prec = !isFinite(+decimals) ? 0 : Math.abs(decimals),
    sep = (typeof thousands_sep === 'undefined') ? ',' : thousands_sep,
    dec = (typeof dec_point === 'undefined') ? '.' : dec_point,
    s = '',
    toFixedFix = function(n, prec) {
      var k = Math.pow(10, prec);
      return '' + Math.round(n * k) / k;
    };
  // Fix for IE parseFloat(0.55).toFixed(0) = 0;
  s = (prec ? toFixedFix(n, prec) : '' + Math.round(n)).split('.');
  if (s[0].length > 3) {
    s[0] = s[0].replace(/\B(?=(?:\d{3})+(?!\d))/g, sep);
  }
  if ((s[1] || '').length < prec) {
    s[1] = s[1] || '';
    s[1] += new Array(prec - s[1].length + 1).join('0');
  }
  return s.join(dec);
}
*/


/*
$(document).ready(function(){
  // Area Chart Example
var ctx = document.getElementById("myAreaChart");
  $.ajax({url: "http://localhost:8000/Staticov/datapatient", success: function(result){
    var myLineChart = new Chart(ctx, {
      type: 'line',
      data: {
        labels: ["0", "10", "20", "30", "40", "50", "60", "70", "80", "90"],
        datasets: [{
          label: "",
          lineTension: 0.3,
          backgroundColor: "rgba(78, 115, 223, 0.5)",
          borderColor: "rgba(78, 115, 223, 1)",
          pointRadius: 3,
          pointBackgroundColor: "rgba(78, 115, 223, 1)",
          pointBorderColor: "rgba(78, 115, 223, 1)",
          pointHoverRadius: 3,
          pointHoverBackgroundColor: "rgba(78, 115, 223, 1)",
          pointHoverBorderColor: "rgba(78, 115, 223, 1)",
          pointHitRadius: 10,
          pointBorderWidth: 2,
          data: result.map(obj => obj),
        }],
      },
      options: {
        maintainAspectRatio: false,
        layout: {
          padding: {
            left: 10,
            right: 25,
            top: 25,
            bottom: 0
          }
        },
        scales: {
          xAxes: [{
            time: {
              unit: 'age'
            },
            gridLines: {
              display: false,
              drawBorder: false
            },
            ticks: {
              maxTicksLimit: 7
            }
          }],
          yAxes: [{
            ticks: {
              maxTicksLimit: 5,
              padding: 10,
              // Include a dollar sign in the ticks
              callback: function(value, index, values) {
                return '' + number_format(value);
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
        },
        legend: {
          display: false
        },
        tooltips: {
          backgroundColor: "rgb(255,255,255)",
          bodyFontColor: "#858796",
          titleMarginBottom: 10,
          titleFontColor: '#6e707e',
          titleFontSize: 14,
          borderColor: '#dddfeb',
          borderWidth: 1,
          xPadding: 15,
          yPadding: 15,
          displayColors: false,
          intersect: false,
          mode: 'index',
          caretPadding: 10,
          callbacks: {
            label: function(tooltipItem, chart) {
              var datasetLabel = chart.datasets[tooltipItem.datasetIndex].label || '';
              return datasetLabel + '' + number_format(tooltipItem.yLabel);
            }
          }
        }
      }
    });
    Chart.defaults.global.defaultFontColor = '#858796';
  }});
  
});

*/


