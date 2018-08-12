    if ($('#logisticDonut').length) {

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
                    data: [document.getElementById("fpl").value, document.getElementById("fnl").value, document.getElementById("tnl").value, document.getElementById("tpl").value],
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
                legend: false,
                responsive: false
            }
        }

        $('#logisticDonut').each(function() {

            var chart_element = $(this);
            var chart_doughnut = new Chart(chart_element, chart_doughnut_settings);

        });

    }