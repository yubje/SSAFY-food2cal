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
              placeholder="아이디를 입력해주세요"
              hide-details
              name="username"
              v-model="UserJoinData.username"
            >
            </v-text-field>
            <!-- ** 아이디 중복체크 버튼 ** -->
            <v-btn
              @click="CheckId"
              class="checkid-btn white--text"
              block 
              depressed 
              color="#FF4500"
              height="48px"
            >
              중복확인
            </v-btn>
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
        password1: null,
        password2: null,
        // weight: null,
        // height: null,
      },
    }
  },
  methods: {
    // ** 아이디 중복체크 **
    CheckId() {
      // this.$http.post(process.env.VUE_SERVER_URL + '/rest-auth/signup/verify-email/')
      this.$http.post('http://8a945e2757a9.ngrok.io' + '/rest-auth/signup/verify-email/')
        .then(res => console.log(res))
        .catch(err => console.log(err))
    },
    // 회원가입
    UserJoin(UserJoinData) {
      if (UserJoinData.username.trim()) {
        if (UserJoinData.password1.trim() === UserJoinData.password2.trim()) {
          this.$http
            .post(process.env.VUE_APP_SERVER_URL + 'rest-auth/signup/', UserJoinData)
            .then(res => {
              this.setCookie(res.data.key)
              this.$router.push({ name: 'Home'})
            })
            // .catch(err => console.log(err))
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
    // join(joinData){
    //   axios.post(SERVER_URL + '/rest-auth/signup/', joinData)
    //   .then(res=>{
    //     this.setCookie(res.data.key)
    //     this.$router.push({name:'Home'})
    //   })
    //   .catch(err=>console.log(err.response))
    // },
  },
  created() {
    console.log(process.env)
  }
}
</script>

<style>
.input_field {
  margin: 6px auto;
}
</style>