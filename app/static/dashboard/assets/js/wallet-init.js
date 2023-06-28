(function ($) {
  // get colors array from the string
  function getChartColorsArray(chartId) {
    var colors = $(chartId).attr("data-colors");
    var coin = $(chartId).attr("coin");
    var data = $(chartId).attr("data");
    var colors = JSON.parse(colors);
    console.log(colors);
    return colors.map(function (value) {
      var newValue = value.replace(" ", "");
      if (newValue.indexOf("--") != -1) {
        var color = getComputedStyle(document.documentElement).getPropertyValue(
          newValue
        );
        if (color && coin) {
          return color, coin;
        }
      } else {
        let value = {
          color: newValue.split(","),
          coin,
          data: JSON.parse(data),
        };
        // console.log();
        return value;
      }
    });
  }

  // coinoverview
  function coinoverview(value, i) {
    var options = {
      chart: {
        type: "bar",
        height: "320",
        stacked: true,
        fontFamily: "Rubik, sans-serif",
        toolbar: {
          show: false,
        },
      },
      series: [
        {
          name: "New Clients",
          data: value[0].data,
        },
      ],

      plotOptions: {
        bar: {
          columnWidth: "25%",
          endingShape: "rounded",
          colors: {
            backgroundBarColors: [
              "#f0f0f0",
              "#f0f0f0",
              "#f0f0f0",
              "#f0f0f0",
              "#f0f0f0",
              "#f0f0f0",
              "#f0f0f0",
              "#f0f0f0",
            ],

            backgroundBarOpacity: 1,
            backgroundBarRadius: 5,
          },
        },
        distributed: true,
      },
      colors: value[0].color,
      grid: {
        show: false,
      },
      legend: {
        show: false,
      },
      fill: {
        opacity: 1,
      },
      dataLabels: {
        enabled: false,
        colors: value[0].color,
        dropShadow: {
          enabled: false,
        },
      },
      xaxis: {
        categories: [
          "01",
          "02",
          "03",
          "04",
          "05",
          "06",
          "07",
          "08",
          "09",
          "10",
          "11",
          "12",
          "13",
        ],
        labels: {
          style: {
            colors: "#787878",
            fontSize: "14px",
            fontFamily: "Rubik, sans-serif",
            fontWeight: 400,
          },
        },
        crosshairs: {
          show: false,
        },
        axisBorder: {
          show: false,
        },
      },
      yaxis: {
        show: true,
        labels: {
          style: {
            colors: "#7E7F80",
            fontSize: "14px",
            fontFamily: "Rubik, sans-serif",
            fontWeight: 400,
            cssClass: "text-uppercase",
          },
          formatter: function (y) {
            return y.toFixed(0) + " " + value[0].coin;
          },
        },
      },
      tooltip: {
        fixed: {
          enabled: false,
        },
        x: {
          show: false,
        },
        y: {
          title: {
            formatter: function (seriesName) {
              return "";
            },
          },
        },
        marker: {
          show: false,
        },
      },
      responsive: [
        {
          breakpoint: 450,
          options: {
            yaxis: {
              show: false,
            },
          },
        },
        {
          breakpoint: 575,
          options: {
            chart: {
              height: 250,
            },
          },
        },
      ],
    };

    var chart = new ApexCharts(
      document.querySelector(`#coinoverviewChart-${i}`),
      options
    );
    chart.render();
  }
  const allcoinoverview = document.querySelectorAll(".coinoverviewCharts");
  for (let i = 0; i < allcoinoverview.length; i++) {
    coinoverview(getChartColorsArray(`#coinoverviewChart-${i}`), i);
  }
})(jQuery);
