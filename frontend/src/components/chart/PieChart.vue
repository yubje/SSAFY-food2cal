<template>
  <div class="pie-chart" :style="pieStyle">

  </div>
</template>

<script>
export default {
  name: 'PieChart',
  props: [
    'pieData'
  ],
  created() {
    console.log(this.pieData)
  },
  computed: {
    pieStyle() {
      let sum = 0
      let styles = this.pieData.map(
        piePart => `${piePart.color} 0 ${sum += piePart.value}%`
      )
      return { background: 'conic-gradient('+ styles.join(",") +')' }
    }
  }
}
</script>

<style lang="scss" scoped>
.pie-chart {
  width: 300px;
  height: 300px;
  border-radius: 50%;
  border: 2px solid #fefefe;
  animation: show 1s ease-in-out;
}

@keyframes show {
  0% {
    transform: scale(0) rotate(720deg);
  }
  100% {
    transform: scale(1) rotate(0deg);
  }
}
</style>