<template>
  <v-container>
    <!-- 유저 정보 -->
    <v-row justify="center">
      <h1>{{ this.username }}</h1>
    </v-row>

    <!-- 식단 통계 -->
    <v-row justify="center">
      <h3>2주 평균 칼로리</h3>
    </v-row>
    <v-row justify="center">
      <div v-if="rerenderflag">
        <Doughnut
          ref="Calorie_Chart"
          :chart-data="this.Caloriedata">
          <!-- :options="options"> -->
        </Doughnut>
      </div>
    </v-row>
    <!-- <v-btn
      @click="GetStatisticsData()"
    >
    다이어트 통계 데이터 받기
    </v-btn> -->

    <div v-if="rerenderflag">
      <line-chart :chart-data="this.datacollection"></line-chart>
      <!-- <v-btn 
        @click="fillData()"
        color="primary">Randomize
      </v-btn> -->
    </div>
  </v-container>
</template>

<script>
// 차트 컴포넌트
import Doughnut from '@/components/chart/Doughnut'
import LineChart from '@/components/chart/LineChart'

// 무작위 컬러 라이브러리
import randomColor from 'randomcolor'

export default {
  name: 'Mypage',
  components: {
    Doughnut,
    LineChart,
  },
  data() {
    return {
      rerenderflag: true,
      username: window.sessionStorage.getItem('username'),
      calories: 0,
      Caloriedata: {
        labels: ['섭취한 평균 칼로리', '절약한 칼로리'],
        datasets: [
          {
            backgroundColor: [randomColor(), '#F84A0D'],
            data: []
          }
        ]
      },
      datacollection: {
        labels: [],
        datasets: [
          {
            label: '탄수화물',
            backgroundColor: ['#0BA40C'],
            data: []
          },
          {
            label: '단백질',
            backgroundColor: ['#FFC30D'],
            data: []
          },
          {
            label: '지방',
            backgroundColor: ['#F84A0D'],
            data: []
          },
        ]
      }
    }
  },

  created() {
    // this.fillData()
    this.GetStatisticsData()
  },

  methods: {
    // 통계 데이터 받아서 갱신하는 함수
    GetStatisticsData() {
      this.calories = 0
      this.$http
        .get(process.env.VUE_APP_SERVER_URL + '/diets/statistics/', 
          { 
            headers: {  
            'X-CSRFToken': this.$cookies.get('csrftoken'),
            'Authorization': `Token ${this.$cookies.get('auth-token')}`
          }
        })
        .then(res => {
          // 일별 영양 성분 정보 정리
          for (const value in res.data) {
            var tandanji = [res.data[value]['carbohydrate'], res.data[value]['protein'], res.data[value]['fat']]
            // 도넛 차트 칼로리 
            this.calories += res.data[value]["calorie"]
            // 라인 차트
            this.datacollection.labels.push(String(value))
            this.datacollection.datasets[0]['data'].push(tandanji[0])
            this.datacollection.datasets[1]['data'].push(tandanji[1])
            this.datacollection.datasets[2]['data'].push(tandanji[2])
          }
          this.Caloriedata.datasets[0]['data'] = [this.calories, window.sessionStorage.getItem('standard')-this.calories]
          this.forceRerender()
        })
        .catch(err => console.log(err))
    },
    forceRerender() {
      this.rerenderflag = false;
      this.$nextTick(() => {
        this.rerenderflag = true;
      })
    },

    // 라인 차트 데이터 테스트 함수
    // fillData() {
    //   this.datacollection = {
    //     labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 
    //       'September', 'October', 'November', 'December'],
    //     datasets: [
    //       {
    //         label: 'Data One',
    //         backgroundColor: '#f87979',
    //         data: [this.getRandomInt(), this.getRandomInt(), this.getRandomInt(), this.getRandomInt(), 
    //           this.getRandomInt(), this.getRandomInt(), this.getRandomInt(), this.getRandomInt(), 
    //           this.getRandomInt(), this.getRandomInt(), this.getRandomInt(), this.getRandomInt()]
    //       }, 
    //       {
    //         label: 'Data Two',
    //         backgroundColor: '#f87979',
    //         data: [this.getRandomInt(), this.getRandomInt()]
    //       }
    //     ]
    //   }
    // },
    getRandomInt () {
      return Math.floor(Math.random() * (50 - 5 + 1)) + 5
    }
  },
}
</script>

<style>

</style>