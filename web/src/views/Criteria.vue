<template>
  <v-row>
    <v-col>
      <v-card class="card-pad" elevation="0" rounded="lg">
        <apexchart
          type="rangeBar"
          height="350"
          :options="timelineData.chartOptions"
          :series="timelineData.series"
        ></apexchart>
      </v-card>
    </v-col>
  </v-row>
</template>

<script>
import { patientsTimeline } from "@/charts/patientsTimeline";

export default {
  data() {
    return {
      timelineData: patientsTimeline(),
    };
  },
};
</script>
