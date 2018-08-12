  if ($('.ActionDonut').length) {
        var chart_doughnut_settings = {
            type: 'doughnut',
            tooltipFillColor: "rgba(51, 51, 51, 0.55)",
            data: {
                labels: [
                    "ALLOW",
                    "DENY",
                    "UNKNOWN"
                ],
                datasets: [{
                    data: [document.getElementById("sallow").value, document.getElementById("sdeny").value, document.getElementById("saction").value],
                    backgroundColor: [
                        "#E74C3C",
                        "#BDC3C7",
                        "#9B59B6"
                        
                       
                       
                    ],
                    hoverBackgroundColor: [
                        "#E95E4F",
                        "#CFD4D8",
                        "#B370CF"
                        
                        
                       
                    ]
                }]
            },
            options: {
                legend: false,
                responsive: false
            }
        }
        $('.ActionDonut').each(function() {
            var chart_element = $(this);
            var chart_doughnut = new Chart(chart_element, chart_doughnut_settings);
        });
    }