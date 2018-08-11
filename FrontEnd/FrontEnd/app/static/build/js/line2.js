if ($("#chart_plot3").length) {
    console.log('Plot1 - testing...');

    var stuff = $("#chart_plot").data('stuff');
    var length = document.getElementById('date_list_length').value;
    console.log(length);
    var data_set=[];

   /* var arr_data1 = [
        [gd(2012, 1, 1), 17],
        [gd(2012, 1, 2), 74],
        [gd(2012, 1, 3), 6],
        [gd(2012, 1, 4), 39],
        [gd(2012, 1, 5), 20],
        [gd(2012, 1, 6), 85],
        [gd(2012, 1, 7), 7]
    ];*/
    for (i =1; i<=length; i++) {
        date = document.getElementById('date'+i+'').value;
       
        count = parseInt(document.getElementById('d_count'+i+'').value);
        console.log(count);

        data_set.push([i,count]);
        }
    console.log("is this here")
    console.log(data_set)

       // console.log()
    /*for (var i = 0; i < 30; i++) {
        chart_plot_02_data.push([
            new Date(Date.today().add(i).days()).getTime(), randNum() + i + i + 10
        ]);
    }*/

    var chart_plot3_settings = {
        series: {
            curvedLines: {
                apply: true,
                active: true,
                monotonicFit: true
            }
        },
        colors: ["#26B99A"],
        grid: {
            borderWidth: {
                top: 0,
                right: 0,
                bottom: 1,
                left: 1
            },
            borderColor: {
                bottom: "#7F8790",
                left: "#7F8790"
            }
        }
    };
    


        $.plot($("#chart_plot3"), [{
            label: "Suspicious Entries",
            data: data_set,
            lines: {
                fillColor: "rgba(150, 202, 89, 0.12)"
            },
            points: {
                fillColor: "#fff"
            }
        }], chart_plot3_settings);

    
}

    