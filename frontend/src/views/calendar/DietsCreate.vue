<template>
  <div>
    <button @click="goToCamera">camera</button>
    <v-col
      cols="12"
      sm="6"
    >
      <v-text-field
        class="p-10"
        v-model="food"
        label="음식을 검색하세요"
        clearable
        @keypress.enter="searchFood"
      ></v-text-field>
    </v-col>
    <div v-if="foodInfo">
      <v-card
        class="mx-auto mt-7"
        max-width="370"
      >
        <v-card-title class="pb-0">
          <div class="d-flex align-center">
            <p class="ml-3 mb-0">{{ foodInfo.food_name }}</p>
          </div>

          <v-container fluid>
            <v-row align="center">
              <v-col
                class="d-flex"
                cols="6"
                sm="6"
              >
                <v-select
                  :items="items"
                  label="Serving"
                  v-model="serving"
                  dense
                ></v-select>
              </v-col>
        
              <v-col
                class="d-flex"
                cols="6"
                sm="6"
              >
                <v-select
                  :items="remains"
                  label="Remain"
                  v-model="remain"
                  dense
                ></v-select>
              </v-col>
            </v-row>
          </v-container>

        </v-card-title>

        <v-card-actions>
          <v-btn text></v-btn>

          <v-btn
            color="purple"
            text
          >
            
          </v-btn>

          <v-spacer></v-spacer>

          <v-btn
            icon
            @click="show = !show"
          >
            <v-icon>{{ show ? 'mdi-chevron-up' : 'mdi-chevron-down' }}</v-icon>
          </v-btn>
        </v-card-actions>

        <v-expand-transition>
          <div v-show="show">
            <v-divider></v-divider>
            
            <v-card-text>
              열량 {{ (serving+remain)*foodInfo.calorie }}kcal
            </v-card-text>
            
            <v-card-text>
              탄수화물 {{ (serving+remain)*foodInfo.carbohydrate }}g
            </v-card-text>
            <v-card-text>
              단백질 {{ (serving+remain)*foodInfo.protein }}g
            </v-card-text>
            <v-card-text>
              지방 {{ (serving+remain)*foodInfo.fat }}g
            </v-card-text>
          </div>
        </v-expand-transition>
      </v-card>
    </div>
    <div v-else>
      <p class="text-center">{{ message }}</p>
    </div>
    <v-btn
      text
      color="primary"
      @click="addDiet"
    >
      Submit
    </v-btn>
  </div>
</template>

<script>
import constants from '@/libs/constants'
import SERVER from '@/libs/api'

export default {
  name: 'DietsCreate',
  data () {
    return {
      show: false,
      food: null,
      items: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
      remains: [0, 0.25, 0.5, 0.75],
      serving: 1,
      remain: 0,
      message: null,
      foodInfo: null
    }
  },
  methods: {
    goToCamera() {
      this.$router.push({ name: constants.URL_TYPE.UPLOAD.CAMERA, query: { date: this.$route.query.date, type: this.$route.query.type } })
    },
    searchFood() {
      const food = {
        food_name: this.food
      }
      this.$http.post(process.env.VUE_APP_SERVER_URL + SERVER.ROUTES.searchFood, food)
        .then(res => {
          if (res.data.message) {
            this.message = '검색 결과가 없습니다.'
            this.foodInfo = null
            return
          }
          this.foodInfo = res.data
        })
    },
    addDiet() {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get(`auth-token`)}`
        }
      }

      const dietData = {
        diet: {
          created_at: this.$route.query.date,
          category: this.$route.query.type,
        },
        food: [
          {
            food_name: this.foodInfo.food_name,
            amount: (this.serving + this.remain) * this.foodInfo.amount,
            calorie: (this.serving + this.remain) * this.foodInfo.calorie,
            carbohydrate: (this.serving + this.remain) * this.foodInfo.carbohydrate,
            protein: (this.serving + this.remain) * this.foodInfo.protein,
            fat: (this.serving + this.remain) * this.foodInfo.fat
          }
        ]
      }
      
      this.$http
        .post(process.env.VUE_APP_SERVER_URL + SERVER.ROUTES.createDiet, dietData, config)
        .then(() => {
          // console.log(res)
          this.isSelectModal = true
        })
        .catch(err => console.log(err.response.data))
    }
  }
}
</script>

<style>

</style>