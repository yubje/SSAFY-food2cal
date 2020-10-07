<template>
  <div>
    <div v-if="isLoading">
      <Loading />
    </div>
    <div v-else>
      <img class="image-area" :src="fileUrl" alt="s3-image">
      <div v-if="!foodInfo.length">
        음식 정보가 없습니다.
      </div>
      <div v-else>
        <div v-for="food in foodInfo" :key="food.id">
          <FoodsInfo :food="food " />
        </div>
      </div>
      <div v-if="$route.query.date" class="d-flex align-center justify-center">
        <v-btn
          color="#F84A0D"
          text
          large
          class="mx-auto"
          @click="addDiet"
        >
          Submit
        </v-btn>
      </div>
      <div v-else class="mt-10">
        <DietModal />
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapState } from 'vuex'
import { routeState } from '@/components/mixins/routeState'
import DietModal from '@/components/common/DietModal'
import FoodsInfo from '@/components/common/FoodsInfo'
import Loading from '@/components/common/Loading'
import SERVER from '@/libs/api'
import constants from '@/libs/constants'

export default {
  name: 'Canvas',
  components: {
    DietModal,
    FoodsInfo,
    Loading
  },
  data() {
    return {
      // show: false,
      // serving: 1,
      // remain: 0,
      // items: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
      // remains: [0, 0.25, 0.5, 0.75],
      AdjFoodInfo: {
        foodName: null,
        gram: 0,
        kcal: 0,
        carbohydrate: 0,
        protein: 0,
        fat: 0
      }
    }
  },
  created() {

  },
  computed: {
    ...mapState([
      'fileUrl',
      'foodInfo',
      'isLoading'
    ]),
    ...mapGetters([
      'LoginFlag'
    ]),
  },
  methods: {
    // setFoodInfo() {
    //   this.AdjFoodInfo.foodName = this.foodInfo.food_name
    //   this.AdjFoodInfo.kcal = (this.serving + this.remain) * this.foodInfo.calorie
    //   this.AdjFoodInfo.carbohydrate = (this.serving + this.remain) * this.foodInfo.carbohydrate
    //   this.AdjFoodInfo.protein = (this.serving + this.remain) * this.foodInfo.protein
    //   this.AdjFoodInfo.fat = (this.serving + this.remain) * this.foodInfo.fat
    // }
    checkLogin() {
      if (!this.LoginFlag) {
        alert('로그인이 필요한 페이지 입니다.')
        this.goToLogin()
        return
      }
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
          standard: window.sessionStorage.getItem('standard')
        },
        food: []
      }

      // if (!this.checkLogin()) {
      //   alert('로그인이 필요한 페이지 입니다.')
      //   this.goToLogin()
      //   return
      // }

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
        .then(() => {
          this.$router.push({ name: constants.URL_TYPE.CALENDAR.DIARY })
        })
        .catch(err => console.log(err.response.data))
    }
  },
  mixins: [
    routeState
  ],
}
</script>

<style scoped>
.image-area {
  width: 100%;
  height: 400px;
}

/* .nutrition {
  padding: 20px;
} */
</style>