<template>
  <v-container>
    <v-row justify="center">
      <v-divider></v-divider>
      <v-col cols="2">
        <v-img 
          src="../../assets/logo.png"
        ></v-img>
      </v-col>
      <v-divider></v-divider>
    </v-row>
    <v-row no-gutters justify="center">
      <v-col cols="3" sm="4"></v-col>
      <v-col cols="6" sm="4" align-self="center" class="m-0">
        <h1 class="text-center">Food To Calorie</h1>
      </v-col>
      <v-col cols="3" sm="4"></v-col>
    </v-row>
    <v-row justify="center" align="center" class="mt-0">
      <!-- 왼쪽 여백 -->
      <v-col cols="2" md="3"></v-col>
      <!-- 로그인 폼 -->
      <v-col cols="8" md="6" class="mt-0">
        <!-- <v-row>
          <v-col cols="1"></v-col>
          <v-img 
            src="../../assets/logo.png"
            width="10"
          >
          </v-img>
          <v-col cols="1" style="padding-left=0px"></v-col>
          <h1>F2C</h1>
          <v-col cols="6"></v-col>
        </v-row> -->
        <v-form name="form" @submit.prevent>
          <div class="input_field">
            <v-text-field
              outlined
              placeholder="이메일"
              hide-details
              name="id"
              v-model="LoginData.username"
            >
            </v-text-field>
          </div>

          <div class="input_field">
            <v-text-field
              @keyup.enter="loginTry(LoginData)"
              type="password"
              outlined
              placeholder="비밀번호"
              hide-details 
              sytle="top:-1px;"
              name="password"
              v-model="LoginData.password"
            >
            </v-text-field>
          </div>
          
          <!-- 테스트 코드 -->
          <!-- <div>
            <v-text-field v-model="LoginData.username">
            </v-text-field>
          </div> -->
          
          
          <!-- ** 아이디/비밀번호 찾기 ** -->
          <!-- <div class="login_append">
            <v-checkbox
              hide-details
              dense
              label="아이디/비밀번호 저장"
              color="#6e8af8"
            ></v-checkbox>
            <span>아이디/비밀번호 찾기</span> 
          </div> -->
          
          <!-- 로그인 버튼 -->
          <div @click="loginTry(LoginData)" class="login-btn">
            <v-btn 
              block 
              depressed 
              color="#FF4500"
              height="48px"
              class="white--text"
            >
              로그인
            </v-btn>
          </div>
          
          <!-- 회원가입 버튼 -->
          <div @click="goToJoin" class="signup-btn">
            <v-btn 
              block 
              depressed 
              color="#FDC06D"
              height="48px"
              class="white--text"
            >
              회원가입
            </v-btn>
          </div>
        </v-form>
      </v-col>


      <!-- 오른쪽 여백 -->
      <v-col cols="2" md="3"></v-col>
    </v-row>
  </v-container>
</template> 

<script>
import constants from '@/libs/constants'
import { mapState, mapActions } from 'vuex'

export default {
  name: 'UsersLogin',
  data() {
    return {
      islogin: false,
      LoginData: {
        username: null,
        password: null,
      },
    }
  },
  computed: {
    ...mapState(["LoginFlag"])
  },
  methods: {
    ...mapActions(["loginTry"]),
    // UserLogin(LoginData) {
    //   if (this.islogin === false) {
    //     if (LoginData.username.trim() && LoginData.password.trim()) {
    //       this.$http
    //         .post(process.env.VUE_APP_SERVER_URL + '/users/login/', LoginData, { headers: { 'X-CSRFToken': this.$cookies.get('csrftoken')}})
    //         .then(res => {
    //           window.sessionStorage.setItem('username', LoginData.username)
    //           this.setCookie(res.data.key)
    //           this.$emit('submit-login')
    //           this.$router.push({ name: 'Home'})
    //         })
    //         .catch(err => console.log(err))
    //     }
    //   } else {
    //     this.$router.push({ name: 'Home'})
    //     alert('이미 로그인 상태입니다.')
    //   }
    // },
    goToJoin() {
      this.$router.push({ name: constants.URL_TYPE.USER.JOIN })
    },
    setCookie(token){
      this.$cookies.set('auth-token',token)
      this.islogin = !this.islogin
    },
  },
  mounted() {
    this.islogin = this.$cookies.isKey('auth-token')
  }
}
</script>

<style>
.login-btn {
  margin: 8px auto;
}
.input_field {
  margin: 6px auto;
}
</style>