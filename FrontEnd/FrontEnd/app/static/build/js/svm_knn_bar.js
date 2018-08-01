if ($('#svm_knn_bar').length){

	var ctx=document.getElementById('svm_knn_bar');
	var mybarChart=new Chart(ctx,{
		type:'bar',

		 data: {
                labels: ["Precision", "Accuracy", "Hits",  "F1Score", "TNR","Miss", "Fallout"],
                datasets: [{
                    label: 'Logistic Regression',
                    backgroundColor: "#26B99A",
                    data: [document.getElementById("svm_p").value,document.getElementById("svm_a").value,
                    document.getElementById("svm_h").value,document.getElementById("svm_s").value,
                    document.getElementById("svm_t").value,document.getElementById("svm_m").value,
                    document.getElementById("svm_f").value]
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

