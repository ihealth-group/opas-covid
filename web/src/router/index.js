import Vue from "vue";
import VueRouter from "vue-router";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    component: () => import("@/views/Index"),
    redirect: "/dashboard",
    children: [
      {
        name: "Dashboard",
        path: "/dashboard",
        component: () => import("@/views/Dashboard"),
      },
      {
        name: "Paciente",
        path: "/patient",
        component: () => import("@/views/Patient"),
      },
    ],
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
