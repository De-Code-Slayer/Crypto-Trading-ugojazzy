(function ($) {
  // get colors array from the string
  function getChartColorsArray(chartId) {
    var colors = $(chartId).attr("data-colors");
    var colors = JSON.parse(colors);
    return colors.map(function (value) {
      var newValue = value.replace(" ", "");
      if (newValue.indexOf("--") != -1) {
        var color = getComputedStyle(document.documentElement).getPropertyValue(
          newValue
        );
        if (color) return color;
      } else {
        return newValue;
      }
    });
  }

  function walletChart() {
    var options = {
      series: [40, 40, 20],
      chart: {
        width: 300,
        type: "pie",
        fontFamily: "Rubik, sans-serif",
      },
      stroke: {
        show: false,
      },
      dataLabels: {
        textAnchor: "middle",
        distributed: false,
        offsetX: 10,
        offsetY: 10,
        enabled: true,
        style: {
          fontSize: "14px",
          fontFamily: "Rubik, sans-serif",
          fontWeight: "normal",
        },
        dropShadow: {
          enabled: false,
        },
      },
      labels: ["Bitcoin", "Ethereum", "Tether"],
      colors: ["#EF8E19", "#5F658B", "#4DAA90"],
      legend: {
        show: false,
      },
    };

    var chart = new ApexCharts(document.querySelector("#walletChart"), options);
    chart.render();
  }
  // Overview
  function overview(color, i) {
    var options = {
      series: [
        {
          data: [2, 10, 18, 22, 36, 15, 47, 25, 15, 19, 14, 2, 47, 42, 15],
        },
      ],
      chart: {
        type: "area",
        height: 50,
        fontFamily: "Rubik, sans-serif",
        sparkline: {
          enabled: true,
        },
      },
      colors: color,
      stroke: {
        curve: "smooth",
        width: 2,
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
    };

    var chart = new ApexCharts(
      document.querySelector(`#overviewChart-${i}`),
      options
    );
    chart.render();
  }
  const allOverview = document.querySelectorAll(".overviewCharts");
  for (let i = 0; i < allOverview.length; i++) {
    overview(getChartColorsArray(`#overviewChart-${i}`), i);
  }
  walletChart();

  // parfectscrollbar
  new PerfectScrollbar("#marketInfo");
  new PerfectScrollbar("#recent-transaction");
  new PerfectScrollbar("#recent-activity");
  new PerfectScrollbar("#announcement");
})(jQuery);
