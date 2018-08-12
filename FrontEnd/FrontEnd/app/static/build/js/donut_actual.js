    if ($('#actualDonut').length) {

        var chart_doughnut_settings = {
            type: 'doughnut',
            tooltipFillColor: "rgba(51, 51, 51, 0.55)",
            data: {
                labels: [
                    " Negative",
                    " Positive"
                   
                ],
                datasets: [{
                    data: [document.getElementById("an").value, document.getElementById("ap").value],
                    backgroundColor: [
                       "#E74C3C",
                        "#26B99A"

                       
                    ],
                    hoverBackgroundColor: [
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

        $('#actualDonut').each(function() {

            var chart_element = $(this);
            var chart_doughnut = new Chart(chart_element, chart_doughnut_settings);

        });

    }