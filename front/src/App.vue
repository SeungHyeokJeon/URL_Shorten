<template>
  <v-app>
    <v-main>
      <UrlShorten/>
    </v-main>
  </v-app>
</template>

<script>
import UrlShorten from './components/UrlShorten';

export default {
  name: 'App',

  components: {
    UrlShorten,
  },

  data: () => ({
    //
  }),
};
</script>
