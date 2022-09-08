export function linesChart() {
  return {
    series: [
      {
        name: "NOT_COVID",
        data: [10, 20, 45],
      },
      {
        name: "COVID_LEVE",
        data: [30, 60, 25],
      },
      {
        name: "SRAG_MODERADO",
        data: [35, 20, 37],
      },
      {
        name: "SRAG_SEVERO",
        data: [98, 45, 63],
      },
    ],
    chartOptions: {
      chart: {
        height: 330,
        type: "line",
        fontFamily: "Roboto Mono, monospace",
        toolbar: { show: false },
      },
      dataLabels: {
        enabled: false,
      },
      stroke: {
        curve: "smooth",
        width: 3.5,
      },
      colors: ["#4CAF50", "#2196F3", "#FFC107", "#F44336"],

      grid: {
        row: {
          colors: ["#f3f3f3", "transparent"], // takes an array which will be repeated on columns
          opacity: 0.5,
        },
      },
      xaxis: {
        categories: ["2021", "2020", "2019"],
      },
    },
  };
}
