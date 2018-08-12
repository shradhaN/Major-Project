// Pie chart
    if ($('#protocol_percent').length) {

        var ctx = document.getElementById("protocol_percent");
        udp=document.getElementById("udp").value;
        tcp=document.getElementById("tcp").value;
        icmp=document.getElementById("icmp").value;
        unknown=document.getElementById("unknown_protocol").value;
        console.log(udp)
        var data = {
            datasets: [{
                data: [udp,tcp,icmp,unknown],
                backgroundColor: [
                    "#455C73",
                    "#9B59B6",
                    "#BDC3C7",
                    "#26B99A"
                ],
                label: 'Protocols' // for legend
            }],
            labels: [
                "UDP",
                "TCP",
                "ICMP",
                "Unknown"
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
