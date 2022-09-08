export function patientHeatmap() {
  return {
    series: [
      {
        name: "152478",
        data: generateData(28, {
          min: 1,
          max: 4,
        }),
      },
    ],
    chartOptions: {
      chart: {
        type: "heatmap",
        fontFamily: "Roboto Mono, monospace",
        toolbar: { show: false },
      },
      plotOptions: {
        heatmap: {
          enableShades: false,
          shadeIntensity: 0,
          radius: 10,
          colorScale: {
            ranges: [
              {
                from: 1,
                to: 1,
                name: "NOT_COVID",
                color: "#4CAF50",
              },
              {
                from: 2,
                to: 2,
                name: "COVID_LEVE",
                color: "#2196F3",
              },
              {
                from: 3,
                to: 3,
                name: "SRAG_MODERADO",
                color: "#FFC107",
              },
              {
                from: 4,
                to: 4,
                name: "SRAG_SEVERO",
                color: "#F44336",
              },
            ],
          },
        },
      },
      yaxis: {
        show: false,
      },
      dataLabels: {
        enabled: false,
      },
      legend: {
        showForSingleSeries: true,
      },
      tooltip: {
        enabled: false,
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
