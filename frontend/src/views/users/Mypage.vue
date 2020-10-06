<template>
  <v-container>
    <div class="Chart">
      <Doughnut
        ref="skills_chart"
        :chart-data="chartData"
        :options="options">
      </Doughnut>
    </div>
    <div>
      <Line
      >
      </Line>
      <button @click="fillData()">Randomize</button>
    </div>
      <line-chart :chart-data="this.datacollection"></line-chart>


    <v-btn
      @click="test()"
    >
    다이어트 통계 데이터 받기
    </v-btn>
  </v-container>
</template>

<script>
// 차트 컴포넌트
import Doughnut from '@/components/chart/Doughnut'
import Line from '@/components/chart/Line'
import LineChart from '@/components/chart/LineChart'

// 무작위 컬러 라이브러리
import randomColor from 'randomcolor'

const options = {
  responsive: true, 
  maintainAspectRatio: false, 
  animation: {
    animateRotate: false
  },
  legend: {
    display: false
  },
  //   tooltips: {
  //       callbacks: {
  //          label: function(tooltipItem) {
  //                 return tooltipItem.yLabel;
  //          }
  //       }
  //   }
}

export default {
  name: 'Mypage',
  components: {
    Doughnut,
    Line,
    LineChart
  },
  data() {
    return {
      calories: [
      ],
      options, 
        chartData: {
        labels: ['탄수화물', '기준 탄수화물'],
        datasets: [
          {
            backgroundColor: [randomColor()],
            data: [1, 2]
          }
        ]
      },
      datacollection: null
    }
  },

  computed: {
    currentDataSet () {
      return this.chartData.datasets[0].data
    }
  },

  created() {
  },

  mounted () {
    this.fillData()
  },

  methods: {
    // Doughnut Chart Data Update
    updateChart () {
      this.$refs.skills_chart.update();
    },
    test() {
      this.$http
        .get(process.env.VUE_APP_SERVER_URL + '/diets/statistics/', 
          { 
            headers: {  
            'X-CSRFToken': this.$cookies.get('csrftoken'),
            'Authorization': `Token ${this.$cookies.get('auth-token')}`
          }
        })
        .then(res => {
          // console.log(typeof(res.data))
          for (const value in res.data) {
            console.log(value, res.data[value])
            this.calories.push(res.data[value]["calorie"])
          }
        })
    },
    fillData() {
      console.log('Click random')
      this.datacollection = {
        labels: [this.getRandomInt(), this.getRandomInt()],
        datasets: [
          {
            label: 'Data One',
            backgroundColor: '#f87979',
            data: [this.getRandomInt(), this.getRandomInt()]
          }, 
          {
            label: 'Data One',
            backgroundColor: '#f87979',
            data: [this.getRandomInt(), this.getRandomInt()]
          }
        ]
      }
      console.log(this.datacollection)
    },
    getRandomInt () {
      return Math.floor(Math.random() * (50 - 5 + 1)) + 5
    }
  },
}
</script>

<style>

</style>