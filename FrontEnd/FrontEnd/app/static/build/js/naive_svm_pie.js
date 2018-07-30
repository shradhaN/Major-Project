    // Pie chart
    if ($('#naive_svm_pie').length) {

        var ctx = document.getElementById("naive_svm_pie");
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
                "Naive",
                "SVM"
             
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
