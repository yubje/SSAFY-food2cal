<template>
  <div>
    <!-- 상단바 -->
    <v-app-bar
      color="#FF890E"
      dark
    >
      <!-- drawer 버튼 -->
      <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>

      <!-- 상단바 여백 -->
      <v-spacer></v-spacer>

      <!-- Search Icon -->
      <v-btn icon>
        <v-icon>mdi-magnify</v-icon>
      </v-btn>
      <v-menu
        left
        bottom
      >
        <template v-slot:activator="{ on, attrs }">
          <v-btn
            icon
            v-bind="attrs"
            v-on="on"
          >
            <v-icon>mdi-dots-vertical</v-icon>
          </v-btn>
        </template>
        <!-- 3 dots 옵션 -->
        <v-list>
          <v-list-item>
            <router-link :to="{ name: constants.URL_TYPE.POST.CREATE, params: {id: 1} }">게시글 작성</router-link>
          </v-list-item>
        </v-list>
      </v-menu>
    </v-app-bar>

    <!-- 사이드바 drawer -->
    <v-navigation-drawer
      v-model="drawer"
      absolute
      left
      temporary
    >
      <!-- 로그인 false -->
      <v-list-item v-if="!LoginFlag" @click="goToLogin" class="avatar-info">
        <!-- 익명 이미지 -->
        <v-list-item-avatar>
          <v-img src="mdi-account"></v-img>
        </v-list-item-avatar>
        <!-- 비로그인 유저 안내 -->
        <v-list-item-content>
          <v-list-item-title>로그인이 필요합니다.</v-list-item-title>
        </v-list-item-content>
      </v-list-item>

      <!-- 로그인 true -->
      <v-list-item v-if="LoginFlag" class="avatar-info">
        <!-- 유저 프로필 이미지 -->
        <v-list-item-avatar>
          <v-img src="https://randomuser.me/api/portraits/men/78.jpg"></v-img>
        </v-list-item-avatar>

        <!-- 유저 닉네임 -->
        <v-list-item-content>
          <v-list-item-title>John Leider</v-list-item-title>
        </v-list-item-content>
      </v-list-item>

      <!-- 하단 구분선 -->
      <v-divider></v-divider>

      <!-- 사이드바 메뉴 리스트 -->
      <v-list
        nav
        dense
      >
        <v-list-item-group
          v-model="group"
          active-class="deep-orange--text text--accent-4"
        >
          <v-list-item @click="goToHome">
            <v-list-item-icon>
              <v-icon>mdi-home</v-icon>
            </v-list-item-icon>
            <v-list-item-title>홈</v-list-item-title>
          </v-list-item>

          <v-list-item @click="goToMypage">
            <v-list-item-icon>
              <v-icon>mdi-account</v-icon>
            </v-list-item-icon>
            <v-list-item-title>내 정보</v-list-item-title>
          </v-list-item>

          <v-list-item>
            <v-list-item-icon>
              <v-icon>mdi-calendar-month</v-icon>
            </v-list-item-icon>
            <v-list-item-title>캘린더</v-list-item-title>
          </v-list-item>

          <v-list-item @click="goToDiary">
            <v-list-item-icon>
              <v-icon>mdi-book-open-outline</v-icon>
            </v-list-item-icon>
            <v-list-item-title>다이어리</v-list-item-title>
          </v-list-item>

          <v-list-item v-if="LoginFlag" @click="logoutTry">
            <v-list-item-icon>
              <v-icon>mdi-logout</v-icon>
            </v-list-item-icon>
            <v-list-item-title>로그아웃</v-list-item-title>
          </v-list-item>

          <v-list-item v-else @click="goToLogin">
            <v-list-item-icon>
              <v-icon>mdi-login</v-icon>
            </v-list-item-icon>
            <v-list-item-title>로그인</v-list-item-title>
          </v-list-item>

        </v-list-item-group>
      </v-list>
    </v-navigation-drawer>
  </div>
</template>

<script>
import constants from '@/libs/constants'
import { mapState, mapActions } from 'vuex'

export default {
  data: () => ({
    constants,
    drawer: false,
    group: null,
    islogin: false,
  }),
  watch: {
    group () {
      this.drawer = false
    },
  },
  methods: {
    ...mapActions(["logoutTry"]),
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
            this.$router.push({ name:'Home'})
          })
      }
    },
    goToLogin() {
      this.$router
        .push({ name: constants.URL_TYPE.USER.LOGIN })
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
    goToMypage() {
      this.$router
        .push({ name: constants.URL_TYPE.USER.MYPAGE })
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
  },
  mounted() {
    this.islogin = this.$cookies.isKey('auth-token')
  },
  computed: {
    ...mapState(["LoginFlag"])
  }
}
</script>

<style>
.avatar-info {
  background-color: #F84A0D;
}
</style>