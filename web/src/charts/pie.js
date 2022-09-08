export function pieChart() {
  return {
    series: [44, 55, 13, 43],
    chartOptions: {
      chart: {
        type: "pie",
        fontFamily: "Roboto Mono, monospace",
      },
      labels: ["NOT_COVID", "COVID_LEVE", "SRAG_MODERADO", "SRAG_SEVERO"],
      colors: ["#4CAF50", "#2196F3", "#FFC107", "#F44336"],
      legend: {
        position: "bottom",
      },
      dataLabels: {
        dropShadow: {
          enabled: false,
        },
      },
      tooltip: {
        fillSeriesColor: false,
      },
    },
  };
}
