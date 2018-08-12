  if ($('.ProtocolDonut').length) {
        var chart_doughnut_settings = {
            type: 'doughnut',
            tooltipFillColor: "rgba(51, 51, 51, 0.55)",
            data: {
                labels: [
                    "UDP",
                    "TCP",
                    "ICMP"
                ],
                datasets: [{
                    data: [document.getElementById("sudp").value, document.getElementById("stcp").value, document.getElementById("sicmp").value],
                    backgroundColor: [
                        "#BDC3C7",
                        "#9B59B6",
                        "#E74C3C"
                       
                       
                    ],
                    hoverBackgroundColor: [
                        "#CFD4D8",
                        "#B370CF",
                        "#E95E4F"
                        
                       
                    ]
                }]
            },
            options: {
                legend: false,
                responsive: false
            }
        }
        $('.ProtocolDonut').each(function() {
            var chart_element = $(this);
            var chart_doughnut = new Chart(chart_element, chart_doughnut_settings);
        });
    }