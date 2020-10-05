<template>
  <div>
    <img class="image-area" :src="fileUrl" alt="s3-image">
    <!-- <div class="nutrition">
      <p>음식: {{ foodInfo.food_name }}</p>
      <p>열량: {{ foodInfo.calorie }} kcal</p>
      <p>양: {{ foodInfo.ammount }} g</p>
      <p>탄수화물: {{ foodInfo.carbohydrate }} g</p>
      <p>단백질: {{ foodInfo.protein }} g</p>
      <p>지방: {{ foodInfo.fat }} g</p>
    </div> -->

    
    <div v-for="food in foodInfo" :key="food.id">
      <v-card
        class="mx-auto mt-7"
        max-width="370"
      >
        <v-card-title class="pb-0">
          <div class="d-flex align-center">
            <p class="ml-3 mb-0">{{ food.food_name }}</p>
          </div>

          <v-container fluid>
            <v-row align="center">
              <v-col
                class="d-flex"
                cols="6"
                sm="6"
              >
                <v-select
                  :items="items"
                  label="Serving"
                  v-model="serving"
                  dense
                ></v-select>
              </v-col>
        
              <v-col
                class="d-flex"
                cols="6"
                sm="6"
              >
                <v-select
                  :items="remains"
                  label="Remain"
                  v-model="remain"
                  dense
                ></v-select>
              </v-col>
            </v-row>
          </v-container>

        </v-card-title>

        <v-card-actions>
          <v-btn text></v-btn>

          <v-btn
            color="purple"
            text
          >
            
          </v-btn>

          <v-spacer></v-spacer>

          <v-btn
            icon
            @click="show = !show"
          >
            <v-icon>{{ show ? 'mdi-chevron-up' : 'mdi-chevron-down' }}</v-icon>
          </v-btn>
        </v-card-actions>

        <v-expand-transition>
          <div v-show="show">
            <v-divider></v-divider>
            
            <v-card-text>
              열량 {{ (serving+remain)*food.calorie }}kcal
            </v-card-text>
            
            <v-card-text>
              탄수화물 {{ (serving+remain)*food.carbohydrate }}g
            </v-card-text>
            <v-card-text>
              단백질 {{ (serving+remain)*food.protein }}g
            </v-card-text>
            <v-card-text>
              지방 {{ (serving+remain)*food.fat }}g
            </v-card-text>
          </div>
        </v-expand-transition>
      </v-card>

    </div>

    <div class="mt-10">
      <DietModal />
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import DietModal from '@/components/common/DietModal'
// import SERVER from '@/libs/api'

export default {
  name: 'Canvas',
  components: {
    DietModal
  },
  data() {
    return {
      show: false,
      serving: 1,
      remain: 0,
      items: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
      remains: [0, 0.25, 0.5, 0.75],
      AdjFoodInfo: {
        foodName: null,
        gram: 0,
        kcal: 0,
        carbohydrate: 0,
        protein: 0,
        fat: 0
      },
    }
  },
  computed: {
    ...mapState([
      'fileUrl',
      'foodInfo'
    ])
  },
  methods: {
    // setFoodInfo() {
    //   this.AdjFoodInfo.foodName = this.foodInfo.food_name
    //   this.AdjFoodInfo.kcal = (this.serving + this.remain) * this.foodInfo.calorie
    //   this.AdjFoodInfo.carbohydrate = (this.serving + this.remain) * this.foodInfo.carbohydrate
    //   this.AdjFoodInfo.protein = (this.serving + this.remain) * this.foodInfo.protein
    //   this.AdjFoodInfo.fat = (this.serving + this.remain) * this.foodInfo.fat
    // }
  },
  mounted() {
    // this.setFoodInfo()
  },
}
</script>

<style scoped>
.image-area {
  width: 100%;
  height: 400px;
}

/* .nutrition {
  padding: 20px;
} */
</style>