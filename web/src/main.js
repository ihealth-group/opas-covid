import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import vuetify from "./plugins/vuetify";
import "./assets/styles/style.scss";

import VueApexCharts from "vue-apexcharts";

Vue.config.productionTip = false;

Vue.use(VueApexCharts);
Vue.component("apexchart", VueApexCharts);

new Vue({
  router,
  store,
  vuetify,
  render: (h) => h(App),
}).$mount("#app");
