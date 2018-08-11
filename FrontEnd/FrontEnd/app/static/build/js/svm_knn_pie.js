    // Pie chart
    if ($('#svm_knn_pie').length) {

        var ctx = document.getElementById("svm_knn_pie");
        var data = {
            datasets: [{
                data: [120, 50],
                backgroundColor: [
                    "#455C73",
                    "#9B59B6"
                   
                ],
                label: 'My dataset' // for legend
            }],
            labels: [
                "Dark Gray",
                "Purple"
             
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