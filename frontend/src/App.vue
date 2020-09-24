<template>
  <v-app>
    <AppBar />
    <v-main class="mb-16">
      <router-view></router-view>
    </v-main>
    <BottomNavbar />
  </v-app>
</template>

<script>
import '@/assets/css/style.css'
import AppBar from '@/components/common/AppBar'
import BottomNavbar from '@/components/common/BottomNavbar'

export default {
  name: 'App',
  components: {
    AppBar,
    BottomNavbar
  },

  data: () => ({
    //
  }),
};
</script>

<style>

</style>
