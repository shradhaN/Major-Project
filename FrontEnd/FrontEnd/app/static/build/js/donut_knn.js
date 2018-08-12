    if ($('#knnDonut').length) {

        var chart_doughnut_settings = {
            type: 'doughnut',
            tooltipFillColor: "rgba(51, 51, 51, 0.55)",
            data: {
                labels: [
                    "False Positive",
                    "False Negative",
                    "True Negative",
                    "True Positive",
                ],
                datasets: [{
                    data: [document.getElementById("fpk").value, document.getElementById("fnk").value, document.getElementById("tnk").value, document.getElementById("tpk").value],
                    backgroundColor: [
                        "#BDC3C7",
                        "#9B59B6",
                        "#E74C3C",
                        "#26B99A"
                       
                    ],
                    hoverBackgroundColor: [
                        "#CFD4D8",
                        "#B370CF",
                        "#E95E4F",
                        "#36CAAB"
                       
                    ]
                }]
            },
            options: {
                legend: true,
                responsive: true
            }
        }

        $('#knnDonut').each(function() {

            var chart_element = $(this);
            var chart_doughnut = new Chart(chart_element, chart_doughnut_settings);

        });

    }