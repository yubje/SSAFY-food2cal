<template>
  <v-row justify="center" class="mx-0">
    <v-dialog v-model="dialog" persistent class="m-0" max-width="600px">
      <template v-slot:activator="{ on, attrs }">
        <v-btn
          color="#F84A0D"
          text
          large
          v-bind="attrs"
          v-on="on"
          class="my-auto"
          @click="checkLogin"
        >
          Submit
        </v-btn>
      </template>
      <v-card>
        <v-card-title>
          <span class="headline">Regist Your Diet</span>
        </v-card-title>
        <v-card-text>
          <v-container>
            <v-row>
              <!-- <v-col cols="12" sm="6" md="4">
                <v-text-field label="Title*" required v-model="title"></v-text-field>
              </v-col>
              <v-col cols="12" sm="6" md="4">
                <v-text-field label="Content*" v-model="content"></v-text-field>
              </v-col> -->
              <v-col cols="12" sm="6">
                <v-select
                  :items="['아침', '점심', '저녁', '간식/기타']"
                  label="Category*"
                  required
                  v-model="category"
                ></v-select>
              </v-col>
            </v-row>
          </v-container>
        </v-card-text>
        <v-card-actions class="d-flex align-center">
          <v-spacer></v-spacer>
          <v-btn color="blue darken-1" text @click="dialog = false; addDiet();">Close</v-btn>
          <v-btn color="blue darken-1" text @click.prevent="dialog = false"><SelectModal /></v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-row>
</template>

<script>
import { mapState } from 'vuex'
import { routeState } from '@/components/mixins/routeState'
import SelectModal from '@/components/common/SelectModal'
import SERVER from '@/libs/api'

export default {
  name: 'DietModal',
  components: {
    SelectModal
  },
  data () {
    return {
      dialog: false,
      title: null,
      content: null,
      category: null,
      diet_image_path: null,
      isSelectModal: false
    }
  },
  computed: {
    ...mapState([
      'fileUrl',
      'foodInfo',
      'LoginFlag'
    ])
  },
  methods: {
    checkLogin() {
      if (!this.LoginFlag) {
        alert('로그인이 필요한 페이지 입니다.')
        this.goToLogin()
        return
      }
    },
    getToday() {
      let time = new Date()
      let year = time.getFullYear()
      let month = time.getMonth() + 1
      month = month >= 10 ? month: '0' + month
      let date = time.getDate()
      date = date >= 10 ? date: '0' + date
      return year + '-' + month + '-' + date
    },
    changeSelectModal() {
      this.isSelectModal = true
    },
    addDiet() {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get(`auth-token`)}`
        }
      }

      let response_category = ''
      if (this.category === '아침') {response_category = 'MO'}
      else if (this.category === '점심') {response_category = 'LU'}
      else if (this.category === '저녁') {response_category = 'DI'}
      else if (this.category === '간식/기타') {response_category = 'SN'}

      const today = this.getToday()

      const dietData = {
        diet: {
          created_at: today,
          category: response_category,
        },
        food: []
      }

      this.foodInfo.forEach(food => {
        dietData.food.push({
          food_name: food.food_name,
          amount: food.amount,
          calorie: food.calorie,
          carbohydrate: food.carbohydrate,
          protein: food.protein,
          fat: food.fat
        })
      })
      
      this.$http
        .post(process.env.VUE_APP_SERVER_URL + SERVER.ROUTES.createDiet, dietData, config)
        .then(res => {
          console.log(res)
          this.isSelectModal = true
        })
        .catch(err => console.log(err.response.data))
    }
  },
  mixins: [
    routeState
  ]
}
</script>