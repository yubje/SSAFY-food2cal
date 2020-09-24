<template>
  <v-container>
    <v-row>
      <!-- 왼쪽 여백 -->
      <v-col cols=4></v-col>
      <!-- 회원가입 폼 -->
      <v-col cols=4>
        <v-form name="form" @submit.prevent style="width:318px">
          <v-text-field
            outlined
            placeholder="아이디를 입력해주세요"
            hide-details
            name="id"
            v-model="UserJoinData.id"
          >
          </v-text-field>
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
          
          <!-- 로그인 버튼 -->
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
      <v-col cols=4></v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: 'UserJoin',
  data() {
    return {
      UserJoinData: {
        id: null,
        password1: null,
        password2: null,
        // weight: null,
        // height: null,
      },
    }
  },
  methods: {
    UserJoin(UserJoinData) {
      if (UserJoinData.id.trim()) {
        console.log(UserJoinData)
      }
    }
    // join(joinData){
    //   axios.post(SERVER_URL + '/rest-auth/signup/', joinData)
    //   .then(res=>{
    //     this.setCookie(res.data.key)
    //     this.$router.push({name:'Home'})
    //   })
    //   .catch(err=>console.log(err.response))
    // },
  }
}
</script>

<style>

</style>