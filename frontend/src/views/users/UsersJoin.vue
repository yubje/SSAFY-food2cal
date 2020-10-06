<template>
  <v-stepper v-model="e1">
    <!-- 스테퍼 헤더 상태 바 -->
    <v-stepper-header>
      <v-stepper-step step="1"
        color="#F84A0D"
        :complete="e1 > 1"
      >
        목표
      </v-stepper-step>

      <v-divider></v-divider>

      <v-stepper-step step="2"
        color="#F84A0D"
        :complete="e1 > 2"
      >
        몸무게
      </v-stepper-step>

      <v-divider></v-divider>

      <v-stepper-step step="3"
        color="#F84A0D"
        :complete="e1 > 3"
      >
        성별
      </v-stepper-step>

      <v-divider></v-divider>

      <v-stepper-step step="4"
        color="#F84A0D"
        :complete="e1 > 4"
      >
        생년월일
      </v-stepper-step>

      <v-divider></v-divider>

      <v-stepper-step step="5"
        color="#F84A0D"
      >
        회원 정보 입력
      </v-stepper-step>
    </v-stepper-header>

    <!-- 스테퍼 내용창 -->
    <v-stepper-items>
      <v-stepper-content step="1">
        <v-row 
          justify="center" 
          class="mb-4"
        >
          <h3>당신의 목표 체중은 얼마인가요?</h3>
        </v-row>
        <v-row
          justify="center" 
          class="mb-4"
        >
          <v-form>
            <v-text-field
              v-model="this.UserJoinData.goal"
              label="체중(kg)"
              type="number"
              color="#FF890E"
            ></v-text-field>
          </v-form>
        </v-row>
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
      <!-- <v-stepper-content step="1">
        <v-row 
          justify="center" 
          class="mb-4"
        >
          <h3>당신의 목표는 무엇인가요?</h3>
        </v-row>
        <v-row
          justify="center" 
          class="mb-4"
        >
          <v-btn
            v-if="this.UserJoinData.goal === '체중 감소'"
            @click="onClickGoal(4)"
            large
            color="#FF890E"
            dark
            elevation="3"
          >
            체중 감소
          </v-btn>
          <v-btn
            v-else
            @click="onClickGoal(1)"
            large
            outlined
            color="#FF890E"
            dark
            elevation="3"
          >
            체중 감소
          </v-btn>
        </v-row>
        <v-row
          justify="center"
          class="mb-4"
        >
          <v-btn
            v-if="this.UserJoinData.goal === '체중 유지'"
            @click="onClickGoal(4)"
            large
            color="#FF890E"
            dark
            elevation="3"
          >
            체중 유지
          </v-btn>
          <v-btn
            v-else
            @click="onClickGoal(2)"
            large
            outlined
            color="#FF890E"
            dark
            elevation="3"
          >
            체중 유지
          </v-btn>
        </v-row>
        <v-row
          justify="center"
          class="mb-4"  
        >
          <v-btn
            v-if="this.UserJoinData.goal === '체중 증가'"
            @click="onClickGoal(4)"
            large
            color="#FF890E"
            dark
            elevation="3"
          >
            체중 증가
          </v-btn>
          <v-btn
            v-else
            @click="onClickGoal(3)"
            large
            outlined
            color="#FF890E"
            dark
            elevation="3"
          >
            체중 증가
          </v-btn>
        </v-row>
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
      </v-stepper-content> -->

      <v-stepper-content step="2">
        <v-row
          justify="center"
          class="mb-4"
        >
          <h3>당신의 키와 몸무게는?</h3>
        </v-row>
        <v-row
          justify="center"
          no-gutters
        >
          <v-form>
            <v-text-field
              v-model="UserJoinData.height"
              label="키(cm)"
              type="number"
              color="#FF890E"
            ></v-text-field>
            <v-text-field
              v-model="UserJoinData.weight"
              label="체중(kg)"
              type="number"
              color="#FF890E"
            ></v-text-field>
          </v-form>
        </v-row>
        <v-btn
          color="primary"
          @click="onClickBodyspec()"
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
        <v-row justify="center">
          <h3>당신의 성별은 무엇인가요?</h3>
        </v-row>
        <v-row 
          justify="center"
          class="mt-5 mb-10"
        >
          <v-col cols=1></v-col>
          <v-col cols=1>
            <v-icon
              v-if="this.UserJoinData.gender==='femail'"
              @click="onClickWoman"
              x-large
              color="#FF890E"
            >mdi-face-woman</v-icon>
            <v-icon 
              v-else
              @click="onClickWoman"
              x-large
            >mdi-face-woman</v-icon>
          </v-col>
          <v-col cols=1 align-self="auto"><div></div></v-col>
          <v-col cols=2>
            <v-icon
              v-if="this.UserJoinData.gender==='mail'"
              @click="onClickMan"
              x-large
              color="#FF890E"
            >mdi-face</v-icon>
            <v-icon 
              v-else
              @click="onClickMan"  
              x-large
            >mdi-face</v-icon>
          </v-col>
        </v-row>
        
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
        <v-row
          justify="center">
          <h3>당신의 생일은 언제인가요?</h3>
        </v-row>
        <v-row 
          class="mt-4"
          justify="center">
          <v-date-picker 
            v-model="UserJoinData.birth"
            locale="ko-kr"
          ></v-date-picker>
        </v-row>
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
        goal: null,
        weight: null,
        height: null,
        birth: new Date().toISOString().substr(0, 10),
        gender: null,
        username: null,
        email: null,
        password1: null,
        password2: null,
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
            .post(process.env.VUE_APP_SERVER_URL + '/users/signup/', UserJoinData)
            .then(() => {
              console.log(UserJoinData)
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
    // 회원가입과 동시에 인증키 쿠키 셋팅
    setCookie(token){
      this.$cookies.set('auth-token',token)
      this.islogin = !this.islogin
    },

    // 성별 입력 메서드
    onClickWoman() {
      // console.log('Click Woman Icon')
      if (this.UserJoinData.gender !== 'femail') {
        this.UserJoinData.gender='femail'
      }
      else {
        this.UserJoinData.gender = null
      } 
    },
    onClickMan() {
      // console.log('Click Man Icon')
      if (this.UserJoinData.gender !== 'mail') {
        this.UserJoinData.gender='mail'
      }
      else {
        this.UserJoinData.gender = null
      }
    },

    // 목표 입력 메서드
    onClickGoal(num) {
      if (num === 1) {
        this.UserJoinData.goal = "체중 감소"
      } else if (num === 2) {
        this.UserJoinData.goal = "체중 유지"
      } else if (num === 3) {
        this.UserJoinData.goal = "체중 증가"
      } else if (num === 4) {
        this.UserJoinData.goal = null
      }
    },

    // 키와 몸무게 입력 메서드(다음 버튼)
    onClickBodyspec() {
      this.e1 = 3
      console.log(this.UserJoinData)
    }
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