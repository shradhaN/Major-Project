 if ($('#knn_naive_line').length) {

        var ctx = document.getElementById("knn_naive_line");
        var lineChart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: ["January", "Feb", "March", "April"],
                datasets: [{
                    label: "Naive",
                    backgroundColor: "rgba(38, 185, 154, 0.31)",
                    borderColor: "rgba(38, 185, 154, 0.7)",
                    pointBorderColor: "rgba(38, 185, 154, 0.7)",
                    pointBackgroundColor: "rgba(38, 185, 154, 0.7)",
                    pointHoverBackgroundColor: "#fff",
                    pointHoverBorderColor: "rgba(220,220,220,1)",
                    pointBorderWidth: 1,
                    data:[document.getElementById("a").value, 10,37,46]
                }, {
                    label: "KNN",
                    backgroundColor: "rgba(3, 88, 106, 0.3)",
                    borderColor: "rgba(3, 88, 106, 0.70)",
                    pointBorderColor: "rgba(3, 88, 106, 0.70)",
                    pointBackgroundColor: "rgba(3, 88, 106, 0.70)",
                    pointHoverBackgroundColor: "#fff",
                    pointHoverBorderColor: "rgba(151,187,205,1)",
                    pointBorderWidth: 1,
                    data: [document.getElementById("b").value, 80, 45,20]
                }]
            },
        });

    }