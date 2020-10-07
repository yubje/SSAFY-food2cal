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
        활동 수준
      </v-stepper-step>

      <v-divider></v-divider>

      <v-stepper-step step="3"
        color="#F84A0D"
        :complete="e1 > 3"
      >
        몸무게
      </v-stepper-step>

      <v-divider></v-divider>

      <v-stepper-step step="4"
        color="#F84A0D"
        :complete="e1 > 4"
      >
        성별
      </v-stepper-step>

      <v-divider></v-divider>

      <v-stepper-step step="5"
        color="#F84A0D"
        :complete="e1 > 5"
      >
        생년월일
      </v-stepper-step>

      <v-divider></v-divider>

      <v-stepper-step step="6"
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
              v-model="goaltmp"
              label="체중(kg)"
              type="number"
              color="#FF890E"
            ></v-text-field>
          </v-form>
        </v-row>
        <v-btn 
          class="white--text"
          color="#0BA40C"
          @click="onClickGoal()"
        >
          다음
        </v-btn>
        <v-btn text
          color="primary"
          @click="goToLogin"
        >
          로그인 화면으로
        </v-btn>
      </v-stepper-content>
      
      <v-stepper-content step="2">
        <v-row 
          justify="center" 
          class="mb-4"
        >
          <h3>당신의 평소 활동 수준은 어느 정도인가요?</h3>
        </v-row>
        <v-row
          justify="center" 
          class="mb-4"
        >
          <v-btn
            v-if="this.UserJoinData.activity === '가벼운 활동'"
            @click="onClickActivity(5)"
            large
            color="#FF890E"
            dark
            elevation="3"
          >
            가벼운 활동
          </v-btn>
          <v-btn
            v-else
            @click="onClickActivity(1)"
            large
            outlined
            color="#FF890E"
            dark
            elevation="3"
          >
            가벼운 활동
          </v-btn>
        </v-row>
        <v-row
          justify="center"
          class="mb-4"
        >
          <v-btn
            v-if="this.UserJoinData.activity === '중등도 활동'"
            @click="onClickActivity(5)"
            large
            color="#FF890E"
            dark
            elevation="3"
          >
            중등도 활동
          </v-btn>
          <v-btn
            v-else
            @click="onClickActivity(2)"
            large
            outlined
            color="#FF890E"
            dark
            elevation="3"
          >
            중등도 활동
          </v-btn>
        </v-row>
        <v-row
          justify="center"
          class="mb-4"  
        >
          <v-btn
            v-if="this.UserJoinData.activity === '강한 활동'"
            @click="onClickActivity(5)"
            large
            color="#FF890E"
            dark
            elevation="3"
          >
            강한 활동
          </v-btn>
          <v-btn
            v-else
            @click="onClickActivity(3)"
            large
            outlined
            color="#FF890E"
            dark
            elevation="3"
          >
            강한 활동
          </v-btn>
        </v-row>
        <v-row
          justify="center"
          class="mb-4"  
        >
          <v-btn
            v-if="this.UserJoinData.activity === '아주 강한 활동'"
            @click="onClickActivity(5)"
            large
            color="#FF890E"
            dark
            elevation="3"
          >
            아주 강한 활동
          </v-btn>
          <v-btn
            v-else
            @click="onClickActivity(4)"
            large
            outlined
            color="#FF890E"
            dark
            elevation="3"
          >
            아주 강한 활동
          </v-btn>
        </v-row>
        <v-btn
          class="white--text"
          color="#0BA40C"
          @click="e1 = 3"
        >
          다음
        </v-btn>
        <v-btn text
          color="primary"
          @click="e1 = 1"
        >
          이전
        </v-btn>
      </v-stepper-content>

      <v-stepper-content step="3">
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
          class="white--text"
          color="#0BA40C"
          @click="onClickBodySpec()"
        >
          다음
        </v-btn>
        <v-btn text
          color="primary"
          @click="e1 = 2"
        >
          이전
        </v-btn>
      </v-stepper-content>

      <v-stepper-content step="4">
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
          class="white--text"
          color="#0BA40C"
          @click="e1 = 5"
        >
          다음
        </v-btn>
        <v-btn text
          color="primary"
          @click="e1 = 3"
        >
          이전
        </v-btn>
      </v-stepper-content>

      <v-stepper-content step="5">
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
            color="orange"
          ></v-date-picker>
        </v-row>
        <v-btn
          class="white--text mr-2"
          color="#0BA40C"
          @click="e1 = 6"
        >
          다음
        </v-btn>
        <v-btn text
          color="primary"
          @click="e1 = 4"
        >
          이전
        </v-btn>
        <v-btn
          @click.prevent="test()">
          프로필 정보 체크
        </v-btn>
      </v-stepper-content>

      <v-stepper-content step="6">
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
                </div>
                <div class="input_field">
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
          @click="e1 = 5"
        >
          이전
        </v-btn>
      </v-stepper-content>
    </v-stepper-items>
  </v-stepper>
</template>

<script>
import constants from '@/libs/constants'

export default {
  name: 'UserJoin',
  data() {
    return {
      e1: 1,
      UserJoinData: {
        username: null,
        password1: null,
        password2: null,
        goal: null,
        weight: undefined,
        height: undefined,
        birth: new Date().toISOString().substr(0, 10),
        gender: null,
        activity: null,
        standard: null,
        profile_image_path: 'pass',
        nickname: null
      },
      goaltmp: undefined,
      kcalValue: null,
    }
  },
  methods: {
    // 회원가입
    UserJoin(UserJoinData) {
      console.log('')
      if (UserJoinData.username && UserJoinData.password1 && UserJoinData.password2) {
        if (UserJoinData.username.trim()) {
          if (UserJoinData.password1.trim() === UserJoinData.password2.trim()) {
            var required_kcal = this.SetupStandard()
            this.UserJoinData.standard = required_kcal-500
            this.$http
              .post(process.env.VUE_APP_SERVER_URL + '/users/signup/', UserJoinData)
              .then(res => {
                const config = {
                  headers: {
                    Authorization: `Token ${res.data.key}`
                  }
                }
                this.UserJoinData.nickname = this.UserJoinData.username
                this.$http
                  .post(process.env.VUE_APP_SERVER_URL + '/users/profiles/', this.UserJoinData, config)
                  .then(() => this.$router.push({ path: '/login' }))
                  .catch(err => console.log(err))
              })
              .catch(err => console.log(err))
          } else {
            alert('비밀번호가 일치하지 않습니다.')
          }
        } else {
          alert('아이디가 비어있습니다.')
        }
      } else {
        alert('아이디, 비밀번호는 필수 입력값입니다.')
      }
    },
    // 성별 입력 메서드
    onClickWoman() {
      if (this.UserJoinData.gender !== 'femail') {
        this.UserJoinData.gender='femail'
      }
      else {
        this.UserJoinData.gender = null
      } 
    },
    onClickMan() {
      if (this.UserJoinData.gender !== 'mail') {
        this.UserJoinData.gender='mail'
      }
      else {
        this.UserJoinData.gender = null
      }
    },
    // 목표 체중 입력 메서드
    onClickGoal() {
      this.e1 = 2
      this.UserJoinData.goal = this.goaltmp
    },
    // 키, 몸무게 입력 메서드
    onClickBodySpec() {
      this.e1 = 4
      this.UserJoinData.goal = Number(this.goaltmp) - Number(this.UserJoinData.weight)
    },
    // 활동 수준 입력 메서드
    onClickActivity(num) {
      if (num === 1) {
        this.UserJoinData.activity = "가벼운 활동"
        this.kcalValue = 25
      } else if (num === 2) {
        this.UserJoinData.activity = "중등도 활동"
        this.kcalValue = 30
      } else if (num === 3) {
        this.UserJoinData.activity = "강한 활동"
        this.kcalValue = 35
      } else if (num === 4) {
        this.UserJoinData.activity = "아주 강한 활동"
        this.kcalValue = 40
      } else if (num) {
        this.UserJoinData.activity = null
        this.kcalValue = null
      }
    },

    goToLogin() {
      this.$router
        .push({ name: constants.URL_TYPE.USER.LOGIN })
    },

    SetupStandard() {
      if (this.gender !== null) {
        if (this.gender === 'male') { return 22*Number(this.UserJoinData.height)**2*this.kcalValue/10000}
        else { return 21*Number(this.UserJoinData.height)**2*this.kcalValue/10000}
      }
    },
    
    test() {
      var required_kcal = this.SetupStandard()
      this.UserJoinData.standard = required_kcal-500
      console.log(this.UserJoinData.standard)
    }
  },
}
</script>

<style>
.input_field {
  margin: 6px auto;
}
</style>