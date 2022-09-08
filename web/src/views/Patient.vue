<template>
  <v-row>
    <v-col>
      <v-row>
        <v-col class="col-12 col-md-3">
          <v-text-field label="ID do paciente" outlined dense append-icon="mdi-magnify"></v-text-field>
        </v-col>
      </v-row>
      <v-row class="mt-0">
        <v-col class="col-12 col-md-3 pt-0">
          <v-card class="card-pad" elevation="0" rounded="lg">
            <div class="d-flex justify-space-between">
              <span class="text-caption">ID do paciente</span>
              <span class="font-weight-bold">152478</span>
            </div>
            <div class="d-flex justify-space-between">
              <span class="text-caption">Notas clínicas</span>
              <span class="font-weight-bold">28</span>
            </div>
          </v-card>
        </v-col>
      </v-row>

      <v-row>
        <v-col>
          <v-card class="card-pad" elevation="0" rounded="lg">
            <h5>Classificação de notas clínicas</h5>
            <apexchart
              type="heatmap"
              height="150"
              :options="heatmapData.chartOptions"
              :series="heatmapData.series"
            ></apexchart>
          </v-card>
        </v-col>
      </v-row>
    </v-col>
  </v-row>
</template>

<script>
import { patientHeatmap } from "@/charts/patientHeatmap";

export default {
  data() {
    return {
      heatmapData: patientHeatmap(),
    };
  },
};
</script>
