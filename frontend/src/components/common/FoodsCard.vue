<template>
  <v-card
    class="mx-auto mt-7"
    max-width="370"
  >
    <v-card-title class="pb-0">
      <div class="d-flex align-center">
        <v-icon>{{ category.icon }}</v-icon>
        <p class="ml-3 mb-0">{{ category.time }}</p>
      </div>
      <v-spacer></v-spacer>
      <v-icon @click="goToDietsCreate">
        mdi-plus-circle-outline
      </v-icon>
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

        <v-card-text v-if="foodInfo && foodInfo[category.type].length">
          <div v-for="food in foodInfo[category.type]" :key="food.id">
            <div class="d-flex justify-space-between align-center">
              <span class="ml-5 text-subtitle-1">{{ food.food_name }}</span>
              <div>
                <span class="mr-3">{{ food.calorie }} kcal</span>
                <v-icon
                  class="mr-5"
                  @click="deleteDiet({'diet_id': food.diet, 'food_id': food.id})"
                >
                  mdi-close-circle-outline
                </v-icon>
              </div>
            </div>
            
  

            <!-- food_name, calorie, carbohydrate, protein, fat -->
            
            
          </div>
        </v-card-text>
        <v-card-text v-else>
          음식 정보가 없습니다.
        </v-card-text>
      </div>
    </v-expand-transition>
  </v-card>
</template>

<script>
import SERVER from '@/libs/api'
import constants from '@/libs/constants'
import { mapActions } from 'vuex'

export default {
  data () {
    return {
      show: false
    }
  },
  props: {
    category: {
      type: Object
    },
    foodInfo: {
      type: Object
    },
    date: {
      type: String
    }
  },
  mounted () {
  },
  methods: {
    ...mapActions([
      'getMonthDiets'
    ]),
    goToDietsCreate() {
      this.$router.push({ name: constants.URL_TYPE.UPLOAD.DIET, query: { date: this.date, type: this.category.type} })
    },
    addDiet() {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get(`auth-token`)}`
        }
      }

      const today = this.date

      const dietData = {
        diet: {
          date: today,
          category: this.category.type,
        },
        food: [
          {
            food_name: this.foodInfo.food_name,
            amount: this.foodInfo.ammount,
            calorie: this.foodInfo.calorie,
            carbohydrate: this.foodInfo.carbohydrate,
            protein: this.foodInfo.protein,
            fat: this.foodInfo.fat
          }
        ]
      }
      this.$http
        .post(process.env.VUE_APP_SERVER_URL + SERVER.ROUTES.createDiet, dietData, config)
        .then(res => {
          console.log(res)
        })
        .catch(err => console.log(err.response.data))
    },
    deleteDiet(food) {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get(`auth-token`)}`
        }
      }

      this.$http
        .delete(process.env.VUE_APP_SERVER_URL + SERVER.ROUTES.createDiet + `${food.diet_id}` + '/foods/' + `${food.food_id}/`, config)
        .then(() => {
          const yearMon = window.localStorage.getItem('yearMon')
          this.getMonthDiets(yearMon)
        })
        .catch(err => {
          console.log(err)
        })
    }
  }
}
</script>

<style scoped>

</style>