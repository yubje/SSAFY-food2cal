<template>
  <v-container v-if="rerenderflag">
    <!-- 유저 정보 -->
    <v-row 
      justify="center"
      class="mt-4 mb-4"
    >
      <h1>{{ this.username }}님의 F2C와 함께한 기록</h1>
    </v-row>

    <!-- 식단 통계 -->
    <v-row justify="center">
      <h2>최근 15일간 평균 칼로리 </h2>
    </v-row>
    <v-row justify="center" class="mt-2">
      <div>
        <Doughnut
          ref="Calorie_Chart"
          :chart-data="this.Caloriedata">
        </Doughnut>
      </div>
    </v-row>


    <div
      v-for="datacollection in datacollections" 
      :key="datacollection.datasets.label"
      class="mt-6 mb-6">
      <v-row class="mt-6">
        <v-col cols=10>
          <h2> {{ datacollection.datasets[0].label }} 섭취량</h2>
        </v-col>
      </v-row>
      <v-row class="mb-2">
        <v-col cols=9>
          <h3> 하루 평균 {{ datacollection.datasets[0].label }} 섭취량: {{ datacollection.avg }}g</h3>
        </v-col>
      </v-row>
      <div>
        <line-chart :chart-data="datacollection"></line-chart>
      </div>
    </div>

  </v-container>
</template>

<script>
// 차트 컴포넌트
import Doughnut from '@/components/chart/Doughnut'
import LineChart from '@/components/chart/LineChart'

// 무작위 컬러 라이브러리
// import randomColor from 'randomcolor'

import { mapActions } from 'vuex'

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
        labels: ['섭취한 일일 칼로리', '절약한 칼로리'],
        datasets: [
          {
            backgroundColor: ['#9AD914', '#F84A0D'],
            data: []
          }
        ]
      },
      datacollections: [
        {
          labels: [],
          datasets: [
            {
              label: '탄수화물',
              backgroundColor: ['#0BA40C'],
              data: []
            },
          ],
          avg: 0
        },
        {
          labels: [],
          datasets: [
            {
              label: '단백질',
              backgroundColor: ['#FFC30D'],
              data: []
            }
          ],
          avg: 0
        },
        {
          labels: [],
          datasets: [
            {
              label: '지방',
              backgroundColor: ['#F84A0D'],
              data: []
            }
          ],
          avg: 0
        }
      ],
      avg_carbohydrate: 0,
      avg_protein: 0,
      avg_fat: 0,
    }
  },

  created() {
    this.getProfile()
    this.GetStatisticsData()
  },

  methods: {
    ...mapActions(['getProfile']),

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
          var data_length = (Object.keys(res.data).length)
          // 일별 영양 성분 정보 정리
          for (const value in res.data) {
            // console.log(res.data[value])
            if (res.data[value]["calorie"] !== 0) {
              var tandanji = [res.data[value]['carbohydrate'], res.data[value]['protein'], res.data[value]['fat']]
              // 도넛 차트 칼로리 
              this.calories += res.data[value]["calorie"]
              // 라인 차트
              this.datacollections[0].labels.push(String(value))
              this.datacollections[1].labels.push(String(value))
              this.datacollections[2].labels.push(String(value))
              this.datacollections[0].datasets[0]['data'].push(tandanji[0])
              this.datacollections[0]['avg'] += tandanji[0]
              this.datacollections[1].datasets[0]['data'].push(tandanji[1])
              this.datacollections[1]['avg'] += tandanji[1]
              this.datacollections[2].datasets[0]['data'].push(tandanji[2])
              this.datacollections[2]['avg'] += tandanji[2]
            } 
          }
          this.Caloriedata.datasets[0]['data'] = [this.calories/(data_length), window.sessionStorage.getItem('standard')-this.calories/(data_length)]
          this.datacollections[0]['avg'] /= parseInt(data_length)
          this.datacollections[1]['avg'] /= parseInt(data_length)
          this.datacollections[2]['avg'] /= parseInt(data_length)

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