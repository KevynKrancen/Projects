
var RELIGION_INDEX = 5;

var COLORS = ["#3e95cd", "#8e5ea2", "#3cba9f"];
var countReligion = {
  "HI": 0,
  "HAR": 0,
  "MASOR": 0,
  "ARA": 0,
  "NOTS": 0,
  "BLI": 0,

}

var keys = {
  "HI": countReligion["HI"],
  "HAR": countReligion["HAR"],
  "MASOR": countReligion["MASOR"],
  "ARA": countReligion["ARA"],
  "NOTS": countReligion["NOTS"],
  "BLI": countReligion["BLI"],

}

function handleData_2(data){
  const labels = Object.values(keys);
  /*const datasets = Object.keys(countReligion);*/

  for(const item of data) {
    countReligion[item[RELIGION_INDEX]] += 1;
  }
  debugger;
  console.log(countReligion)
  new Chart(document.getElementById("doughnut-chart"), {
    type: 'doughnut',
    data: {
      labels : ["חרדי", "חילוני", "ערבי", "נוצרי", "מסורתי", "ללא דת"],
      datasets: [{
        label : labels,
        backgroundColor: ["#3e95cd", "#8e5ea2","#3cba9f","#e8c3b9","#808000","#c45850"],
        data: [countReligion["HI"],countReligion["HAR"],countReligion["MASOR"],countReligion["ARA"],countReligion["NOTS"],countReligion["BLI"]],
      }]
    },
    options: {
      title: {
        display: true,
        text: 'נתוני נדבקים 2020 - ע"פ דת'
      },
    }
  });

   /*return {
    data: Object.values(countReligion),
    label: keys,
    borderColor: COLORS[index % COLORS.length],
    fill: false
  }*/
}

function handleError(error){
  console.log({error});
}

$.ajax({url:"http://localhost:8000/Staticov/datapatient", success: handleData_2, error: handleError});