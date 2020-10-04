<template>
  <v-stepper v-model="e1">
    <!-- 스테퍼 헤더 상태 바 -->
    <v-stepper-header>
      <v-stepper-step step="1"
        :complete="e1 > 1"
      >
        목표
      </v-stepper-step>

      <v-divider></v-divider>

      <v-stepper-step step="2"
        :complete="e1 > 2"
      >
        몸무게
      </v-stepper-step>

      <v-divider></v-divider>

      <v-stepper-step step="3"
        :complete="e1 > 3"
      >
        성별
      </v-stepper-step>

      <v-divider></v-divider>

      <v-stepper-step step="4"
        :complete="e1 > 4"
      >
        생년월일
      </v-stepper-step>

      <v-divider></v-divider>

      <v-stepper-step step="5">
        회원 정보 입력
      </v-stepper-step>
    </v-stepper-header>

    <!-- 스테퍼 내용창 -->
    <v-stepper-items>
      <v-stepper-content step="1">
        <v-card
          class="mb-12"
          color="grey lighten-1"
          height="200px"
        ></v-card>
        <!-- 버튼 -->
        <v-btn
          color="primary"
          @click="e1 = 2"
        >
          다음
        </v-btn>
        <v-btn text
          color="primary"
        >
          로그인 화면으로
        </v-btn>
      </v-stepper-content>

      <v-stepper-content step="2">
        <v-card
          class="mb-12"
          color="grey lighten-1"
          height="200px"
        ></v-card>
        <!-- 버튼 -->
        <v-btn
          color="primary"
          @click="e1 = 3"
        >
          다음
        </v-btn>
        <v-btn text
          @click="e1 = 1"
        >
          이전
        </v-btn>
      </v-stepper-content>

      <v-stepper-content step="3">
        <v-card
          class="mb-12"
          color="grey lighten-1"
          height="200px"
        ></v-card>

        <!-- 버튼 -->
        <v-btn
          color="primary"
          @click="e1 = 4"
        >
          다음
        </v-btn>
        <v-btn text
          @click="e1 = 2"
        >
          이전
        </v-btn>
      </v-stepper-content>
      <v-stepper-content step="4">
        <v-row justify="center">
          <v-col cols=12>
            <h3>당신의 생일은 언제인가요?</h3>
          </v-col>
          <v-col cols=12>
            <v-date-picker 
            v-model="UserJoinData.birth"
            locale="ko-kr"
          ></v-date-picker>
          </v-col>
        </v-row>
        <!-- 버튼 -->
        <v-btn
          color="primary"
          @click="e1 = 5"
        >
          다음
        </v-btn>
        <v-btn text
          @click="e1 = 3"
        >
          이전
        </v-btn>
      </v-stepper-content>

      <v-stepper-content step="5">
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
                    name="username"
                    v-model="UserJoinData.username"
                  >
                  </v-text-field>
                </div>
                <div class="input_field">
                  <v-text-field
                    outlined
                    placeholder="이메일을 입력해주세요"
                    hide-details
                    name="email"
                    v-model="UserJoinData.email"
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
                
                <!-- 회원가입 버튼 -->
                <div @click="UserJoin(UserJoinData)" class="login_btn">
                  <v-btn 
                    block 
                    depressed 
                    color="#FF4500"
                    height="48px"
                    class="white--text"
                    rounded
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
        <!-- 버튼 -->
        <v-btn text
          @click="e1 = 4"
        >
          이전
        </v-btn>
      </v-stepper-content>
    </v-stepper-items>

    
  </v-stepper>
</template>

<script>
export default {
  name: 'UserJoin',
  data() {
    return {
      e1: 1,
      UserJoinData: {
        username: null,
        email: null,
        password1: null,
        password2: null,
        // weight: null,
        // goal: null,
        // height: null,
        birth: new Date().toISOString().substr(0, 10),
        // gender: null,
        // preference: null,
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
      // if (UserJoinData)
      if (UserJoinData.username.trim()) {
        if (UserJoinData.password1 === UserJoinData.password2) {
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
        alert('닉네임이 비어있습니다.')
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