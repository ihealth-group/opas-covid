<template>
  <v-card class="card-pad" elevation="0" rounded="lg">
    <h5>Classificação de notas clínicas</h5>
    <apexchart
      type="heatmap"
      height="150"
      :options="heatmapData.chartOptions"
      :series="heatmapData.series"
    ></apexchart>
  </v-card>
</template>

<script>
export default {
  props: {
    data: Array,
    showPatientId: Boolean,
  },
  data() {
    return {};
  },
};
</script>
