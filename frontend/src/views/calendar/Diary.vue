<template>
  <div>
    <Calendar />
    <FoodsCard :category="{ time: '아침', icon: 'mdi-weather-sunset-up' }" />
    <FoodsCard :category="{ time: '점심', icon: 'mdi-white-balance-sunny' }" />
    <FoodsCard :category="{ time: '저녁', icon: 'mdi-weather-sunset' }" />
    <FoodsCard :category="{ time: '간식/기타', icon: 'mdi-theme-light-dark' }" />
  </div>
</template>

<script>
import FoodsCard from '@/components/common/FoodsCard'
import Calendar from '@/components/common/Calendar'

export default {
  name: 'Diary',
  components: {
    FoodsCard,
    Calendar
  }
}
</script>

<style>

</style>