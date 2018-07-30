if ($('#naive_svm_bar').length){

	var ctx=document.getElementById('naive_svm_bar');
	var mybarChart=new Chart(ctx,{
		type:'bar',
		data:{
			labels:["Naive","svm"],
			datasets:[{
				label:[["Naive"],["svm"]],
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

