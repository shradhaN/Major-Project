if ($('#knn_naive_bar').length){

	var ctx=document.getElementById('knn_naive_bar');
	var mybarChart=new Chart(ctx,{
		type:'bar',
		
		 data: {
                labels: ["Precision", "Accuracy", "Hits", "Miss", "Fallout", "F1Score", "TNR"],
                datasets: [{
                    label: 'Naive',
                    backgroundColor: "#26B99A",
                    data: [document.getElementById("naive_p").value,document.getElementById("naive_a").value,
                    document.getElementById("naive_h").value,document.getElementById("naive_s").value,
                    document.getElementById("naive_t").value,document.getElementById("naive_m").value,
                    document.getElementById("naive_f").value]
                }, {
                    label: 'KNN',
                    backgroundColor: "#03586A",
                    data: [document.getElementById("knn_p").value,document.getElementById("knn_a").value,
                    document.getElementById("knn_h").value,document.getElementById("knn_s").value,
                    document.getElementById("knn_t").value,document.getElementById("knn_m").value,
                    document.getElementById("knn_f").value]
                }]
            },
		 options: {
                scales: {
                    yAxes: [{
                        ticks: {
                            beginAtZero: true
                        }
                    }]
                }
            }

	});
}

