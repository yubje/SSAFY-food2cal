<template>
  <div>
    <Calendar @select-date="updateFoodInfo" @date="updateDate" />
    <div v-if="foodInfo">
      {{ foodInfo.calorie }}
      {{ foodInfo.carbohydrate }}
      {{ foodInfo.protein }}
      {{ foodInfo.fat }}
    </div>
    
    <FoodsCard :category="{ time: '아침', icon: 'mdi-weather-sunset-up', type: 'MO' }" :foodInfo="foodInfo" :date="date" />
    <FoodsCard :category="{ time: '점심', icon: 'mdi-white-balance-sunny', type: 'LU' }" :foodInfo="foodInfo" :date="date" />
    <FoodsCard :category="{ time: '저녁', icon: 'mdi-weather-sunset', type: 'DI' }" :foodInfo="foodInfo" :date="date" />
    <FoodsCard :category="{ time: '간식/기타', icon: 'mdi-theme-light-dark', type: 'SN' }" :foodInfo="foodInfo" :date="date" />
  </div>
</template>

<script>
import FoodsCard from '@/components/common/FoodsCard'
import Calendar from '@/components/common/Calendar'

export default {
  name: 'Diary',
  data () {
    return {
      foodInfo: null,
      date: null
    }
  },
  components: {
    FoodsCard,
    Calendar
  },
  methods: {
    updateFoodInfo(foodInfo) {
      this.foodInfo = foodInfo
      console.log(this.foodInfo)
    },
    updateDate(date) {
      this.date = date
      console.log(this.date)
    }
  }
}
</script>

<style>

</style>