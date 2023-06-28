(function ($) {
  var radialChart = function () {
    var options = {
      series: [70],
      chart: {
        height: 130,
        width: 100,
        type: "radialBar",
        fontFamily: "Rubik, sans-serif",
      },
      plotOptions: {
        radialBar: {
          hollow: {
            margin: 0,
            size: "65%",
            background: "#0e6eff ",
          },
          track: {
            show: false,
          },

          dataLabels: {
            show: true,
            value: {
              color: "#fff",
              offsetY: -8,
              fontSize: "16px",
              show: true,
              fontWeight: "500",
            },
          },
        },
      },
      fill: {
        colors: ["#fff", "#fff"],
      },
      stroke: {},
      labels: [""],
    };

    var chart = new ApexCharts(document.querySelector("#radialChart"), options);
    chart.render();
  };
  radialChart();
})(jQuery);
