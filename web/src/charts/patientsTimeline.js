export function patientsTimeline() {
  return {
    series: [
      {
        name: "NOT_COVID",
        data: [
          {
            x: "158528",
            y: [new Date("2019-03-01").getTime(), new Date("2020-03-01").getTime()],
          },
        ],
      },
      {
        name: "COVID_LEVE",
        data: [
          {
            x: "105863",
            y: [new Date("2019-04-01").getTime(), new Date("2019-06-01").getTime()],
          },
        ],
      },
      {
        name: "SRAG_SEVERO",
        data: [
          {
            x: "258963",
            y: [new Date("2019-05-01").getTime(), new Date("2019-09-01").getTime()],
          },
        ],
      },
    ],
    chartOptions: {
      chart: {
        height: 350,
        type: "rangeBar",
        fontFamily: "Roboto Mono, monospace",
      },
      plotOptions: {
        bar: {
          horizontal: true,
          barHeight: "50%",
          rangeBarGroupRows: true,
        },
      },
      colors: ["#4CAF50", "#2196F3", "#F44336"],
      fill: {
        type: "solid",
      },
      xaxis: {
        type: "datetime",
      },
      legend: {
        position: "top",
      },
      // tooltip: {
      //   custom: function (opts) {
      //     const fromYear = new Date(opts.y1).getFullYear();
      //     const toYear = new Date(opts.y2).getFullYear();
      //     const values = opts.ctx.rangeBar.getTooltipValues(opts);

      //     return "";
      //   },
      // },
    },
  };
}
