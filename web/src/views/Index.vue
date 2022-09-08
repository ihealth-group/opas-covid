<template>
  <v-app>
    <v-app-bar app flat color="white">
      <v-container fluid class="py-0 fill-height">
        <v-btn v-for="link in links" :key="link.name" text :to="link.to" class="mr-2">
          {{ link.name }}
        </v-btn>
      </v-container>
    </v-app-bar>

    <v-main class="grey lighten-3 pa-0">
      <v-container fluid>
        <v-scroll-x-transition mode="out-in">
          <router-view />
        </v-scroll-x-transition>
      </v-container>
    </v-main>

    <v-footer app min-height="60">
      <p class="text-body-2 mb-0">
        Projeto de pesquisa envolvendo instituições como HCPA, GHC, OPAS/OMS e outros hospitais
      </p>
    </v-footer>
  </v-app>
</template>

<script>
export default {
  data: () => ({
    links: [
      { name: "Dashboard", to: "/dashboard" },
      { name: "Paciente", to: "/patient" },
    ],
  }),
};
</script>
