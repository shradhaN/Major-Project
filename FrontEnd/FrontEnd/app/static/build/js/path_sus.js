  if ($('.PathDonut').length) {
        var chart_doughnut_settings = {
            type: 'doughnut',
            tooltipFillColor: "rgba(51, 51, 51, 0.55)",
            data: {
                labels: [
                    "RECEIVE",
                    "SEND",
                    "ICMP"
                ],
                datasets: [{
                    data: [document.getElementById("sreceive").value, document.getElementById("ssend").value, document.getElementById("spath").value],
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
        $('.PathDonut').each(function() {
            var chart_element = $(this);
            var chart_doughnut = new Chart(chart_element, chart_doughnut_settings);
        });
    }