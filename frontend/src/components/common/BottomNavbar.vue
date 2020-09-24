<template>
  <v-bottom-navigation
    :value="activeBtn"
    fixed
    color="#FF890E"
  >
    <v-btn @click="goToCamera">
      <span>Camera</span>
      <v-icon>mdi-camera</v-icon>
    </v-btn>

    <v-btn @click="goToHome">
      <span>Home</span>
      <v-icon>mdi-home</v-icon>
    </v-btn>

    <v-btn>
      <span>Calendar</span>
      <v-icon>mdi-calendar</v-icon>
    </v-btn>

    <v-btn @click="goToLogin">
      <span>Login</span>
      <v-icon>mdi-pencil</v-icon>
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
      this.$router
        .push({ name: constants.URL_TYPE.UPLOAD.CAMERA })
        .catch(err => {
          if(err.name != "NavigationDuplicated" ){
            throw err
          }
        })
    },
    goToHome() {
      this.$router
        .push('/')
        .catch(err => {
          if(err.name != "NavigationDuplicated" ){
            throw err
          }
        })
    },
    goToLogin() {
      this.$router
        .push({ name: constants.URL_TYPE.USER.LOGIN })
        .catch(err => {
          if(err.name != "NavigationDuplicated" ){
            throw err
          }
        })
    }
  }
}
</script>

<style>

</style>