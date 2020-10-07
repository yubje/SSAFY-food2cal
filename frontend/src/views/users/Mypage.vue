<template>
  <v-container>
    <v-row justify="center">
      <h3>평균 칼로리</h3>
    </v-row>
    <v-row>
      
      <div class="">
        <Doughnut
          ref="Calorie_Chart"
          :chart-data="ChartData"
          :options="options">
        </Doughnut>
      </div>
    </v-row>

    <!-- <div>
      <Line
      >
      </Line>
    </div> -->

    <div>
      <line-chart :chart-data="this.datacollection"></line-chart>
      <v-btn 
        @click="fillData()"
        color="primary">Randomize</v-btn>
    </div>

    <!-- <div>
      <reactive :chart-data="datacollection"></reactive>
    </div> -->

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
// import Line from '@/components/chart/Line'
import LineChart from '@/components/chart/LineChart'
// import Reactive from '@/components/chart/Reactive'

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
    // Line,
    LineChart,
    // Reactive
  },
  data() {
    return {
      calories: [
      ],
      options,
      ChartData: {
        labels: ['일일 평균 칼로리', '기준 칼로리'],
        datasets: [
          {
            backgroundColor: [randomColor()],
            data: [2, 1]
          }
        ]
      },
      datacollection: null
    }
  },

  created() {
    this.fillData()
  },

  mounted () {
  },

  methods: {
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
          console.log(res)
          for (const value in res.data) {
            console.log(value, res.data[value])
            this.calories.push(res.data[value]["calorie"])
          }
        })
    },
    fillData() {
      this.datacollection = {
        labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 
          'September', 'October', 'November', 'December'],
        datasets: [
          {
            label: 'Data One',
            backgroundColor: '#f87979',
            data: [this.getRandomInt(), this.getRandomInt(), this.getRandomInt(), this.getRandomInt(), 
              this.getRandomInt(), this.getRandomInt(), this.getRandomInt(), this.getRandomInt(), 
              this.getRandomInt(), this.getRandomInt(), this.getRandomInt(), this.getRandomInt()]
          }, 
          {
            label: 'Data Two',
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