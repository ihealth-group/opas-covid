export function heatmapChart() {
  return {
    series: [
      {
        name: "NOT_COVID",
        data: generateData(36, {
          min: 0,
          max: 90,
        }),
      },
      {
        name: "COVID_LEVE",
        data: generateData(36, {
          min: 0,
          max: 90,
        }),
      },
      {
        name: "SRAG_MODERADO",
        data: generateData(36, {
          min: 0,
          max: 90,
        }),
      },
      {
        name: "SRAG_SEVERO",
        data: generateData(36, {
          min: 0,
          max: 90,
        }),
      },
    ],
    chartOptions: {
      chart: {
        height: 600,
        type: "heatmap",
        fontFamily: "Roboto Mono, monospace",
        toolbar: { show: false },
      },
      plotOptions: {
        heatmap: {
          shadeIntensity: 1,
          radius: 10,
          min: 0,
          max: 90,
        },
      },
      dataLabels: {
        enabled: false,
      },
      colors: ["#4CAF50", "#2196F3", "#FFC107", "#F44336"],
      tooltip: {
        enabled: true,
        y: {
          show: true,
          formatter: (val) => `${val} pacientes`,
        },
      },
      xaxis: {
        type: "category",
        categories: [
          "Jan/2021",
          "Fev/2021",
          "Mar/2021",
          "Abr/2021",
          "Mai/2021",
          "Jun/2021",
          "Jul/2021",
          "Ago/2021",
          "Set/2021",
          "Out/2021",
          "Nov/2021",
          "Dez/2021",
          "Jan/2020",
          "Fev/2020",
          "Mar/2020",
          "Abr/2020",
          "Mai/2020",
          "Jun/2020",
          "Jul/2020",
          "Ago/2020",
          "Set/2020",
          "Out/2020",
          "Nov/2020",
          "Dez/2020",
          "Jan/2019",
          "Fev/2019",
          "Mar/2019",
          "Abr/2019",
          "Mai/2019",
          "Jun/2019",
          "Jul/2019",
          "Ago/2019",
          "Set/2019",
          "Out/2019",
          "Nov/2019",
          "Dez/2019",
        ],
      },
      grid: {
        padding: {
          right: 20,
        },
        yaxis: {
          lines: {
            show: false,
          },
        },
      },
    },
  };
}

function generateData(count, yrange) {
  var i = 0;
  var series = [];
  while (i < count) {
    var x = (i + 1).toString();
    var y = Math.floor(Math.random() * (yrange.max - yrange.min + 1)) + yrange.min;
    series.push({
      x: x,
      y: y,
    });
    i++;
  }
  return series;
}
