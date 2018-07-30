if ($('#three_algo_bar').length){

	var ctx=document.getElementById('three_algo_bar');
	var mybarChart=new Chart(ctx,{
		type:'bar',
		data:{
			labels:["Naive","KNN", "SVM"],
			datasets:[{
				label:[["Naive"],["KNN"],["SVM"]],
				backgroundColor:["#1abc9c ","#34495e","#acadac"],
				data:[document.getElementById("ref_m_count").value,
				document.getElementById("ref_f_count").value,
				document.getElementById("a").value,]
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

