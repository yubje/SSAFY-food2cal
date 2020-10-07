<template>
  <div v-if="dietMonthInfo">
    <!-- <Calendar @food-info="updateFoodInfo" @date="updateDate" /> -->
    <Calendar @date="updateDate" />
    <div v-if="dietMonthInfo[date]"  class="mx-5">
      <p class="text-center text-h5"><strong>하루 섭취 열량</strong></p>
      <v-progress-linear color="#FFC30D" :value="dietMonthInfo[date].calorie / setStandard * 100" height="20">
        <strong>{{ Math.ceil(dietMonthInfo[date].calorie / setStandard * 100) }}%</strong>
      </v-progress-linear>
      
      <p class="text-center mt-7">탄수화물 {{ dietMonthInfo[date].carbohydrate }}g</p>
      <p class="text-center">단백질 {{ dietMonthInfo[date].protein }}g</p>
      <p class="text-center">지방 {{ dietMonthInfo[date].fat }}g</p>
      <!-- <PieChart :pieData="pieStyle" /> -->
    </div>
    <!-- <FoodsCard :category="{ time: '아침', icon: 'mdi-weather-sunset-up', type: 'MO' }" :foodInfo="dietMonthInfo[setToday]" :date="date" /> -->
    <FoodsCard :category="{ time: '아침', icon: 'mdi-weather-sunset-up', type: 'MO' }" :date="date" />
    <FoodsCard :category="{ time: '점심', icon: 'mdi-white-balance-sunny', type: 'LU' }" :date="date" />
    <FoodsCard :category="{ time: '저녁', icon: 'mdi-weather-sunset', type: 'DI' }" :date="date" />
    <FoodsCard :category="{ time: '간식/기타', icon: 'mdi-theme-light-dark', type: 'SN' }" :date="date" />
  </div>
</template>

<script>
import FoodsCard from '@/components/common/FoodsCard'
import Calendar from '@/components/common/Calendar'
// import PieChart from '@/components/chart/PieChart'
import { mapState, mapActions } from 'vuex'

export default {
  name: 'Diary',
  data () {
    return {
      // foodInfo: null,
      date: null,
      userStandard: 0,
      isLoading: false
    }
  },
  components: {
    FoodsCard,
    Calendar,
    // PieChart
  },
  created() {
    this.getMonthDiets(window.localStorage.getItem('yearMon'))
    this.date = window.localStorage.getItem('date')
  },
  mounted() {
  },
  computed: {
    ...mapState([
      'dietMonthInfo'
    ]),
    setToday() {
      return window.localStorage.getItem('date')
    },
    setStandard() {
      return window.sessionStorage.getItem('standard')
    }
    // pieStyle() {
    //   let carbohydrate = this.dietMonthInfo.carbohydrate
    //   let protein = this.dietMonthInfo.protein
    //   let fat = this.dietMonthInfo.fat
    //   console.log(carbohydrate)
    //   return [
    //     { color: '#0B6487', value: carbohydrate },
    //     { color: '#9D1F37', value: protein },
    //     { color: '#F6931C', value: fat },
    //   ]
    // }
  },
  methods: {
    ...mapActions([
      'getMonthDiets'
    ]),
    // updateFoodInfo(foodInfo) {
    //   this.foodInfo = foodInfo
    //   console.log(this.foodInfo)
    // },
    updateDate(date) {
      window.localStorage.setItem('date', date)
      this.date = date
      console.log(this.date)
    }
  }
}
</script>

<style scoped>
.v-sheet--offset {
  top: -24px;
  position: relative;
}
</style>