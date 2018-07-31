if ($('#naive_svm_bar').length){

	var ctx=document.getElementById('naive_svm_bar');
	var mybarChart=new Chart(ctx,{
		type:'bar',
		
		 data: {
                labels: ["Precision", "Accuracy", "Hits", "Miss", "Fallout", "F1Score", "TNR"],
                datasets: [{
                    label: 'SVM',
                    backgroundColor: "#26B99A",
                    data: [document.getElementById("svm_p").value,document.getElementById("svm_a").value,
                    document.getElementById("svm_h").value,document.getElementById("svm_s").value,
                    document.getElementById("svm_t").value,document.getElementById("svm_m").value,
                    document.getElementById("svm_f").value]
                }, {
                    label: 'Naive',
                    backgroundColor: "#03586A",
                    data: [document.getElementById("naive_p").value,document.getElementById("naive_a").value,
                    document.getElementById("naive_h").value,document.getElementById("naive_s").value,
                    document.getElementById("naive_t").value,document.getElementById("naive_m").value,
                    document.getElementById("naive_f").value]
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

