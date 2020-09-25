<template>
  <v-container>
    <v-row justify="center" align="center">
      <!-- 왼쪽 여백 -->
      <v-col cols="2" md="3"></v-col>
      <!-- 회원가입 폼 -->
      <v-col cols="8" md="6">
        <v-form name="form" @submit.prevent>
          <div class="input_field">
            <v-text-field
              outlined
              placeholder="닉네임을 입력해주세요"
              hide-details
              name="email"
              v-model="UserJoinData.email"
            >
            </v-text-field>
          </div>
          <div class="input_field">
            <v-text-field
              outlined
              placeholder="이메일을 입력해주세요"
              hide-details
              name="username"
              v-model="UserJoinData.username"
            >
            </v-text-field>
            <!-- ** 이메일 중복체크 버튼 ** -->
            <!-- <v-btn
              v-if="!emailflag"
              @click="CheckEmail"
              class="checkemail-btn white--text"
              block 
              depressed 
              color="#FF4500"
              height="48px"
            >
              이메일 중복확인
            </v-btn> -->
          </div>
          <div class="input_field">
            <v-text-field
              @keyup.enter="login"
              type="password"
              outlined
              placeholder="패스워드를 입력해주세요"
              hide-details 
              sytle="top:-1px;"
              name="password"
              v-model="UserJoinData.password1"
            >
            </v-text-field>
          </div>
          <div class="input_field">
            <v-text-field
              @keyup.enter="login"
              type="password"
              outlined
              placeholder="패스워드를 한 번 더 입력해주세요"
              hide-details 
              sytle="top:-1px;"
              name="password"
              v-model="UserJoinData.password2"
            >
            </v-text-field>
          </div>
          
          <!-- 아이디/비밀번호 찾기 -->
          <!-- <div class="login_append">
            <v-checkbox
              hide-details
              dense
              label="아이디/비밀번호 저장"
              color="#6e8af8"
            ></v-checkbox>
            <span>아이디/비밀번호 찾기</span> 
          </div> -->
          
          <!-- 회원가입 버튼 -->
          <div @click="UserJoin(UserJoinData)" class="login_btn">
            <v-btn 
              block 
              depressed 
              color="#FF4500"
              height="48px"
              class="white--text"
            >
              Join to F2C
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
export default {
  name: 'UserJoin',
  data() {
    return {
      UserJoinData: {
        username: null,
        email: null,
        password1: null,
        password2: null,
        // weight: null,
        // height: null,
      },
      // emailflag: false
    }
  },
  methods: {
    // ** 이메일 중복체크 **
    // CheckEmail() {
    //   this.$http
    //     .post(process.env.VUE_APP_SERVER_URL + 'rest-auth/signup/verify-email/', {'Key': this.UserJoinData.email})
    //     .then(res => {
    //       console.log(res)
    //       this.emailflag =! this.emailflag  
    //     })
    //     .catch(err => console.log(err))
    // },
    // 회원가입
    UserJoin(UserJoinData) {
      if (UserJoinData.username.trim()) {
        if (UserJoinData.password1.trim() === UserJoinData.password2.trim()) {
          this.$http
            .post(process.env.VUE_APP_SERVER_URL + '/rest-auth/signup/', UserJoinData)
            .then(() => {
              // this.setCookie(res.data.key)
              this.$router.push({ name: 'Home'})
            })
            .catch(err => console.log(err))
        } else {
          alert('비밀번호가 일치하지 않습니다.')
        }
      } else {
        alert('아이디가 비어있습니다.')
      }
    },
    setCookie(token){
      this.$cookies.set('auth-token',token)
      this.islogin = !this.islogin
    },
  },
}
</script>

<style>
.input_field {
  margin: 6px auto;
}
.checkemail-btn {
  margin: 6px auto;
}
</style>