<template>
  <v-container>
    <v-card
      class="mx-auto text-center"
      color="green"
      dark
      max-width="600"
    >
      <!-- 제목 -->
      <v-card-title>
        <!-- 아이콘 -->
        <!-- <v-icon
          :color="checking ? 'red lighten-2' : 'indigo'"
          class="mr-12"
          size="64"
          @click="takePulse"
        >
          mdi-heart-pulse
        </v-icon> -->


        <v-row align="start">
          <div class="caption grey--text text-uppercase">
            <span
              class="display-1 font-color-white"
              color="white">
              칼로리
            </span>
            
          </div>
          <!-- <div>
            <span
              class="display-2 font-weight-black"
              v-text="avg || '—'"
            ></span>
            <strong v-if="avg">BPM</strong>
          </div> -->
        </v-row>

        <v-spacer></v-spacer>

        <!-- 디테일 화살표 -->
        <!-- <v-btn
          icon
          class="align-self-start"
          size="28"
        >
          <v-icon>mdi-arrow-right-thick</v-icon>
        </v-btn> -->
      </v-card-title>

      <!-- 카드 내용 -->
      <v-card-text>
        <v-sheet color="rgba(0, 0, 0, .12)">
          <v-sparkline
            :value="dates"
            color="rgba(255, 255, 255, .7)"
            height="100"
            padding="24"
            stroke-linecap="round"
            smooth
          >
            <template v-slot:label="item">
              ${{ item.value }}
            </template>
          </v-sparkline>
        </v-sheet>
      </v-card-text>

      <!-- <v-card-text>
        <div class="display-1 font-weight-thin">
          Sales Last 24h
        </div>
      </v-card-text> -->

      <v-divider></v-divider>

      <!-- <v-card-actions class="justify-center">
        <v-btn
          block
          text
        >
          Go to Report
        </v-btn>
      </v-card-actions> -->
    </v-card>
    <button class="button" @click="addExperience">Add experience</button>
    <div class="Chart">
      <Doughnut
        ref="skills_chart"
        :chart-data="chartData"
        :options="options">
      </Doughnut>

      <div v-for="(val, i) in currentDataSet" :key="i">
        <input
          type="range" 
          min="0" 
          max="8"
          placeholder="name"
          :value="currentDataSet[i]"
          @input="updateAmount($event.target.value, i)"
        >
        <span>
          {{ currentDataSet[i] }} years
        </span>
        <input type="text" :value="chartData.labels[i]" @input="updateName($event.target.value, i)">
        <button @click="remove(i)">remove</button>
      </div>

    </div>
  </v-container>
</template>

<script>
//
import Doughnut from '@/components/chart/Doughnut'
// 무작위 컬러 라이브러리
import randomColor from 'randomcolor'

const options = {
  responsive: true, 
  maintainAspectRatio: false, 
  animation: {
    animateRotate: false
  }
}

export default {
  name: 'Mypage',
  components: {
    Doughnut
  },
  data() {
    return {
      dates: [
        423,
        446,
        675,
        510,
        590,
        610,
        760,
      ],
      options, 
        chartData: {
        labels: ['skill1'],
        datasets: [
          {
            backgroundColor: [randomColor()],
            data: [1]
          }
        ]
      }
    }
  },

  computed: {
    currentDataSet () {
      return this.chartData.datasets[0].data
    }
  },

  created() {
  },

  methods: {
    // Doughnut Chart Data
    updateChart () {
      this.$refs.skills_chart.update();
    },
    updateAmount (amount, index) {
      this.chartData.datasets[0].data.splice(index, 1, amount)
      this.updateChart();
    },
    updateName (text, index) {
      this.chartData.labels.splice(index, 1, text)
      this.updateChart();
    },
    addExperience() {
      const currentDataset = this.chartData.datasets[0]
      this.chartData.labels.push(`Skill ${currentDataset.data.length + 1}`)
      currentDataset.data.push(0)
      currentDataset.backgroundColor.push(randomColor())
      this.updateChart();
    },
    remove (index) {
      const currentDataset = this.chartData.datasets[0]
      currentDataset.data.splice(index, 1)
      this.chartData.labels.splice(index, 1)
      currentDataset.backgroundColor.splice(index, 1)
      this.updateChart()
    }
  },
}
</script>

<style>

</style>