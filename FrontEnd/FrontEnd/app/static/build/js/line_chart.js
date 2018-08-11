

function gd(year, month, day) {
    return new Date(year, month - 1, day).getTime();
}
function parse(dateString){
  var parts = dateString.split("-");
  console.log("inparse")
  console.log(parts)
  return ([parts[2], parts[1], parts[0]]);
}


if ($("#chart_plot").length) {
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
        date_=parse(date)
        date_day = date_[0]
        date_month = date_[1]
        date_year = date_[2]
        console.log(date_);
        console.log(date_year)
        console.log(date_month)
        console.log(date_day)

        count = parseInt(document.getElementById('d_count'+i+'').value);
        console.log(count);

        data_set.push([gd(parseInt(date_year),parseInt(date_month),parseInt(date_day)),count]);
        }
    console.log("is this here")
    console.log(data_set)

       // console.log()
    /*for (var i = 0; i < 30; i++) {
        chart_plot_02_data.push([
            new Date(Date.today().add(i).days()).getTime(), randNum() + i + i + 10
        ]);
    }*/

    var chart_plot_settings = {
        series: {
            lines: {
                show: false,
                fill: true
            },
            splines: {
                show: true,
                tension: 0.4,
                lineWidth: 1,
                fill: 0.4
            },
            points: {
                radius: 0,
                show: true
            },
            shadowSize: 2
        },
        grid: {
            verticalLines: true,
            hoverable: true,
            clickable: true,
            tickColor: "#d5d5d5",
            borderWidth: 1,
            color: '#fff'
        },
        colors: ["rgba(38, 185, 154, 0.38)", "rgba(3, 88, 106, 0.38)"],
        xaxis: {
            tickColor: "rgba(51, 51, 51, 0.06)",
            mode: "time",
            tickSize: [1, "day"],
            //tickLength: 10,
            axisLabel: "Date",
            axisLabelUseCanvas: true,
            axisLabelFontSizePixels: 12,
            axisLabelFontFamily: 'Verdana, Arial',
            axisLabelPadding: 10
        },
        yaxis: {
            ticks: 8,
            tickColor: "rgba(51, 51, 51, 0.06)",
        },
        tooltip: true
    };

    

        $.plot($("#chart_plot"), data_set, chart_plot_settings);
    }

