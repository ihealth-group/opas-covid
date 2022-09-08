export function timelineChart() {
  return {
    series: [
      {
        name: "NOT_COVID",
        data: [
          {
            x: "MAIS CASOS",
            y: [new Date("2019-03-01").getTime(), new Date("2019-03-31").getTime()],
          },
          {
            x: "MENOS CASOS",
            y: [new Date("2020-06-01").getTime(), new Date("2020-06-30").getTime()],
          },
        ],
      },
      {
        name: "COVID_LEVE",
        data: [
          {
            x: "MAIS CASOS",
            y: [new Date("2020-03-01").getTime(), new Date("2020-03-31").getTime()],
          },
          {
            x: "MENOS CASOS",
            y: [new Date("2019-06-01").getTime(), new Date("2019-06-30").getTime()],
          },
        ],
      },
      {
        name: "SRAG_MODERADO",
        data: [
          {
            x: "MAIS CASOS",
            y: [new Date("2021-02-01").getTime(), new Date("2021-02-28").getTime()],
          },
          {
            x: "MENOS CASOS",
            y: [new Date("2019-04-01").getTime(), new Date("2019-04-30").getTime()],
          },
        ],
      },
      {
        name: "SRAG_SEVERO",
        data: [
          {
            x: "MAIS CASOS",
            y: [new Date("2021-02-01").getTime(), new Date("2021-02-28").getTime()],
          },
          {
            x: "MENOS CASOS",
            y: [new Date("2021-11-01").getTime(), new Date("2021-11-30").getTime()],
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
        },
      },
      dataLabels: {
        enabled: false,
      },
      colors: ["#4CAF50", "#2196F3", "#FFC107", "#F44336"],
      xaxis: {
        type: "datetime",
      },
      legend: {
        position: "bottom",
      },
    },
  };
}
