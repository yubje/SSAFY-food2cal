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
    <chartjs-doughnut
      :labels="doughnut.labels"
      :datasets="doughnut.datasets"
      :option="options"
    ></chartjs-doughnut>
  </v-container>
</template>

<script>
export default {
  name: 'Mypage',
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
      doughnut: {
        datasets: [{
          data: [10, 20, 30]
        }],

        // These labels appear in the legend and in the tooltips when hovering different arcs
        labels: [
          'Red',
          'Yellow',
          'Blue'
        ]
      },
      options: {
        title: {
          display: true,
          position: "bottom",
          text: "Fruits"
        }
      }
    }
  },

  computed: {
  },

  created() {
  },

  methods: {
  },
}
</script>

<style>

</style>