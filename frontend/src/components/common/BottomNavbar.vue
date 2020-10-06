<template>
  <v-bottom-navigation
    :value="activeBtn"
    fixed
    color="#FF890E"
    class="mt-10"
  >
    <v-btn @click="goToCamera" class="px-0">
      <span>Camera</span>
      <v-icon>mdi-camera</v-icon>
    </v-btn>

    <v-btn @click="goToHome">
      <span>Home</span>
      <v-icon>mdi-home</v-icon>
    </v-btn>

    <!-- <v-btn>
      <span>Calendar</span>
      <v-icon>mdi-calendar</v-icon>
    </v-btn> -->

    <!-- 로그인(false) -->
    <v-btn v-if="!this.islogin" @click="goToLogin">
      <span>Login</span>
      <v-icon>mdi-login</v-icon>
    </v-btn>

    <v-btn v-else @click="goToMypage">
      <span>Mypage</span>
      <v-icon>mdi-account</v-icon>
    </v-btn>

    <!-- 마이페이지(true) -->
    <!-- <v-btn v-if="this.islogin" @click="goToMypage">
      <span>Mypage</span>
      <v-icon>mdi-pencil</v-`icon>
    </v-btn> -->

    <v-btn @click="goToDiary">
      <span>Diary</span>
      <v-icon>mdi-book-open-outline</v-icon>
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
      islogin: false,
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
          if(err.name != "NavigationDuplicated" ) throw err
        })
    },
    goToDiary() {
      this.$router
        .push({ name: constants.URL_TYPE.CALENDAR.DIARY })
        .catch(err => {
          if(err.name != "NavigationDuplicated" ){
            throw err
          }
        })
    },
    goToMypage() {
      this.$router
        .push({ name: constants.URL_TYPE.USER.MYPAGE })
        .catch(err => {
          if(err.name != "NavigationDuplicated" ) throw err
        })
    },
    UserLogout() {
      const config = {
        headers: {'Authorization': `Token ${this.$cookies.get('auth-token')}`}
      }
      if (this.islogin === true) {
        this.$http
          .post(process.env.VUE_APP_SERVER_URL + '/rest-auth/logout/', null, config)
          .catch(err=>console.log(err.response))
          .finally(() => {
            this.$cookies.remove('auth-token')
            this.$emit('submit-logout')
            this.islogin != this.islogin
            this.$router.push({ name:'home'})
          })
      }
    }
  },
  mounted() {
    this.islogin = this.$cookies.isKey('auth-token')
  },
  computed() {
    this.islogin = this.$cookies.isKey('auth-token')
  }
}
</script>

<style>

</style>