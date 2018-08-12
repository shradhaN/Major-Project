if ($('#three_algo_line').length) {
    
    var length = document.getElementById('date_list_length').value;
    var un_length = document.getElementById('date_list_length_un').value;
    

    count_number=[]
    date_array=[]
    for (i =1; i<=length; i++) {
        date = document.getElementById('date'+i+'').value;
        date_array.push(date)       
        count = parseInt(document.getElementById('d_count'+i+'').value);
        count_number.push(count)
        }

    count_unsus=[]
    date_unsus=[]

    for (i =1; i<=un_length; i++) {
        date = document.getElementById('date_un'+i+'').value;
        date_unsus.push(date)       
        count = parseInt(document.getElementById('d_count_un'+i+'').value);
        count_unsus.push(count)
        }

    console.log()

    /*if date_unsus.length>date_array.length{
        date=date_unsus;
    }
    else:
        date=date_array;*/

    
        var ctx = document.getElementById("three_algo_line");
        var lineChart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: date_unsus,
                datasets: [{
                    label: "Suspicious",
                    backgroundColor: "rgba(255,0,0, 0.31)",
                    borderColor: "rgba(255,0,0, 0.7)",
                    pointBorderColor: "rgba(255,0,0, 0.7)",
                    pointBackgroundColor: "rgba(255,0,0, 0.7)",
                    pointHoverBackgroundColor: "#fff",
                    pointHoverBorderColor: "rgba(220,220,220,1)",
                    pointBorderWidth: 1,
                    data:count_number
                },
      {
                    label: "Unsuspicious",
                    backgroundColor: "rgba(3, 88, 106, 0.31)",
                    borderColor: "rgba(3, 88, 106, 0.70)",
                    pointBorderColor: "rgba(3, 88, 106, 0.70)",
                    pointBackgroundColor: "rgba(3, 88, 106, 0.70)",
                    pointHoverBackgroundColor: "#fff",
                    pointHoverBorderColor: "rgba(151,187,205,1)",
                    pointBorderWidth: 1,
                    data:count_unsus
                }]
            },
        });
    }