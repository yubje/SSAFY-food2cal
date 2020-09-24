<template>
  <v-container>
    <v-row justify="center" align="center">
      <!-- 왼쪽 여백 -->
      <v-col cols="2" md="3"></v-col>


      <!-- 로그인 폼 -->
      <v-col cols="8" md="6">
        <h1>F2C</h1>
        <v-form name="form" @submit.prevent>
          <div class="input_field">
            <v-text-field
              outlined
              placeholder="아이디"
              hide-details
              name="id"
              v-model="LoginData.username"
            >
            </v-text-field>
          </div>

          <div class="input_field">
            <v-text-field
              @keyup.enter="UserLogin(LoginData)"
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
          <div @click="UserLogin(LoginData)" class="login-btn">
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

export default {
  name: 'UsersLogin',
  data() {
    return {
      islogin: false,
      LoginData: {
        username: null,
        password: null
      },
    }
  }, // 9b32cef1b0714379dc2839ac826ada74fd059e53
  methods: {
    UserLogin(LoginData) {
      if (this.islogin === false) {
        if (LoginData.username.trim() && LoginData.password.trim()) {
          this.$http
            .post(process.env.VUE_APP_SERVER_URL + 'rest-auth/login/', LoginData)
            .then(res => {
              this.setCookie(res.data.key)
              this.$router.push({ name: 'Home'})
            })
            .catch(err => console.log(err))
        }
      } else {
        alert('이미 로그인 상태입니다.')
      }
    },
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