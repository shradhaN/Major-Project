    // Pie chart
    if ($('#three_algo_pie').length) {

        var ctx = document.getElementById("three_algo_pie");
        var data = {
            datasets: [{
                data: [120, 50,45],
                backgroundColor: [
                    "#455C73",
                    "#9B59B6",
                    "#1abc9c "
                   
                ],
                label: 'My dataset' // for legend
            }],
            labels: [
                "Naive",
                "SVM",
                "KNN"
             
            ]
        };

        var pieChart = new Chart(ctx, {
            data: data,
            type: 'pie',
            otpions: {
                legend: false
            }
        });

    }
