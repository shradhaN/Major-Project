if ($('#pieChart_percent').length) {

        var ctx = document.getElementById("pieChart_percent");
        sus = document.getElementById('sus_percent').value;
        unsus = document.getElementById('unsus_percent').value;
        console.log(sus)
        console.log(unsus)
        var data = {
            datasets: [{
                data: [unsus,sus],
                backgroundColor: [
                    "#9B59B6",
                    "#455C73",
                    
                    
                ],
                label: 'My dataset' // for legend
            }],
            labels: [
                "Unsuspicious",
                "Suspicious"            ]
        };

        var pieChart = new Chart(ctx, {
            data: data,
            type: 'pie',
            otpions: {
                legend: false
            }
        });
    };
