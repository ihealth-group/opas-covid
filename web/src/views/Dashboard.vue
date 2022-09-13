<template>
  <v-row>
    <v-col>
      <v-row>
        <v-col class="col-12 col-md-3">
          <v-card class="card-pad h-100 d-flex align-center justify-center" elevation="0" rounded="lg">
            <apexchart
              type="pie"
              height="320"
              :options="pieData.chartOptions"
              :series="pieData.series"
            ></apexchart>
          </v-card>
        </v-col>
        <v-col class="col-12 col-md-4 pl-0">
          <v-card class="card-pad" elevation="0" rounded="lg">
            <apexchart
              type="line"
              height="330"
              :options="lineData.chartOptions"
              :series="lineData.series"
            ></apexchart>
          </v-card>
        </v-col>
        <v-col class="col-12 col-md-5 pl-0">
          <v-card class="card-pad" elevation="0" rounded="lg">
            <apexchart
              type="rangeBar"
              height="330"
              :options="timelineData.chartOptions"
              :series="timelineData.series"
            ></apexchart>
          </v-card>
        </v-col>
      </v-row>

      <v-row>
        <v-col class="pt-0">
          <v-card class="card-pad" elevation="0" rounded="lg">
            <div class="heatmap-chart">
              <apexchart
                type="heatmap"
                height="350"
                width="2000"
                :options="heatmapData.chartOptions"
                :series="heatmapData.series"
              ></apexchart>
            </div>
          </v-card>
        </v-col>
      </v-row>
    </v-col>
  </v-row>
</template>

<script>
import { pieChart } from "@/charts/pie";
import { linesChart } from "@/charts/lines";
import { timelineChart } from "@/charts/timeline";
import { heatmapChart } from "@/charts/heatmap";

export default {
  data() {
    return {
      pieData: pieChart(),
      lineData: linesChart(),
      timelineData: timelineChart(),
      heatmapData: heatmapChart(),
    };
  },
};
</script>
