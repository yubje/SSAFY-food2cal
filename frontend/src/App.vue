<template>
  <v-app>
    <AppBar
      v-if="rerenderflag"
      @submit-logout="forceRerender"
    />
    <v-main class="mb-16">
      <router-view 
        :key="$route.fullPath"
        @submit-login="forceRerender"
      ></router-view>
    </v-main>
    <BottomNavbar
      v-if="rerenderflag"
      @submit-logout="forceRerender"
    />
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
    rerenderflag:true,
  }),
  methods: {
    forceRerender() {
        this.rerenderflag = false;
        this.$nextTick(() => {
          this.rerenderflag = true;
        })
      },
  }
};
</script>

<style>

</style>
