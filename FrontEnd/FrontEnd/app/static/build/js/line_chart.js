


if ($("#chart_plot").length) {
    console.log('Plot1 - testing...');

    var stuff = $("#chart_plot").data('stuff');
    var length = document.getElementById('date_list_length');
    var data_set=[];
    for (i =1; i<=length; i++) {
        date = document.getElementById('date'+i+'');
        count = document.getElementById('d_count'+I+'');
        data_set.push([date,count]);
        concole.log(data_set)
    }
    // alert(stuff);
    var chart_plot_02_settings = {
        grid: {
            show: true,
            aboveData: true,
            color: "#3f3f3f",
            labelMargin: 10,
            axisMargin: 0,
            borderWidth: 0,
            borderColor: null,
            minBorderMargin: 5,
            clickable: true,
            hoverable: true,
            autoHighlight: true,
            mouseActiveRadius: 100
        },
        series: {
            lines: {
                show: true,
                fill: true,
                lineWidth: 2,
                steps: false
            },
            points: {
                show: true,
                radius: 4.5,
                symbol: "circle",
                lineWidth: 3.0
            }
        },
        legend: {
            position: "ne",
            margin: [0, -25],
            noColumns: 0,
            labelBoxBorderColor: null,
            labelFormatter: function(label, series) {
                return label + '&nbsp;&nbsp;';
            },
            width: 40,
            height: 1
        },
        colors: ['#96CA59', '#3F97EB', '#72c380', '#6f7a8a', '#f7cb38', '#5a8022', '#2c7282'],
        shadowSize: 0,
        tooltip: true,
        tooltipOpts: {
            content: "%s: %y.0",
            xDateFormat: "%d/%m",
            shifts: {
                x: -30,
                y: -50
            },
            defaultTheme: false
        },
        yaxis: {
            min: 0
        },
        xaxis: {
            mode: "time",
            minTickSize: [1, "day"],
            timeformat: "%d/%m/%y",
            min: data_set[''][0],
            max: data_set[3][0]
        }
    };


    // console.log()
    

    $.plot($("#chart_plot"), [data_set], chart_plot_02_settings);
};

