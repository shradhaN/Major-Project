


if ($("#chart_plot").length) {
    console.log('Plot1 - testing...');

    var stuff = $("#chart_plot").data('stuff');
    var length = document.getElementById('date_list_length').value;
    console.log(length);
    var data_set=[];
    for (i =1; i<=length; i++) {
        date = document.getElementById('date'+i+'').value;
        console.log(date);
        count = document.getElementById('d_count'+i+'').value;
        console.log(count);
        data_set.push([date,count]);
        }
    console.log("is this here")
    console.log(data_set)

       // console.log()
    var chart_plot_03_settings = {
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

    $.plot($("#chart_plot"), [{
            label: "Registrations",
            data: data_set,
            lines: {
                fillColor: "rgba(150, 202, 89, 0.12)"
            },
            points: {
                fillColor: "#fff"
            }
        }], chart_plot_03_settings);
};

