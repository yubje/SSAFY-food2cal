<template>
  <v-bottom-navigation
    :value="activeBtn"
    fixed
    color="#FF890E"
  >
    <v-btn>
      <span>Recents</span>
      <v-icon>mdi-history</v-icon>
    </v-btn>

    <v-btn @click="goToCamera">
      <span>Camera</span>
      <v-icon>mdi-camera</v-icon>
    </v-btn>
    
    <v-btn>
      <span>Calendar</span>
      <v-icon>mdi-calendar</v-icon>
    </v-btn>
  </v-bottom-navigation>
</template>

<script>
import constants from '@/libs/constants'

export default {
  name: 'BottomNavbar',
  components: {
    
  },
  data () {
    return {
      constants,
      activeBtn: 1,
    }
  },
  methods: {
    goToCamera() {
      this.$router.push({ name: constants.URL_TYPE.UPLOAD.CAMERA })
    }
  }
}
</script>

<style>

</style>