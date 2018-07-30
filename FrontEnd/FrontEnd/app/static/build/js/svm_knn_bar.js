if ($('#svm_knn_bar').length){

	var ctx=document.getElementById('svm_knn_bar');
	var mybarChart=new Chart(ctx,{
		type:'bar',
		data:{
			labels:["SVM","KNN"],
			datasets:[{
				label:[["SVM"],["KNN"]],
				backgroundColor:["#abb2b9 ","#1abc9c"],
				data:[document.getElementById("ref_m_count").value,document.getElementById("ref_f_count").value]
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

