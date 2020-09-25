<template>
  <div>
    <img class="image-area" :src="fileUrl" alt="s3-image">
    <div class="nutrition">
      <p>음식: {{ foodInfo.food_name }}</p>
      <p>열량: {{ foodInfo.calorie }} kcal</p>
      <p>양: {{ foodInfo.ammount }} g</p>
      <p>탄수화물: {{ foodInfo.carbohydrate }} g</p>
      <p>단백질: {{ foodInfo.protein }} g</p>
      <p>지방: {{ foodInfo.fat }} g</p>
    </div>
    
    <div class="m-0">
      <PostsModal />
    </div>
  </div>
</template>

<script>
// import axios from 'axios'
import { mapState } from 'vuex'
import PostsModal from '@/components/common/PostsModal'

export default {
  name: 'Canvas',
  data() {
    return {
      
    }
  },
  components: {
    PostsModal
  },
  computed: {
    ...mapState([
      'fileUrl',
      'foodInfo'
    ])
  },
  methods: {
    // sendUrl(fileUrl) {
    //   console.log(fileUrl)
    //   axios.get('http://8a945e2757a9.ngrok.io/predict/', fileUrl)
    //     .then((res) => {
    //       console.log(res.data.amount)
    //     })
    // },
  },
  beforeMount() {
    // this.sendUrl(this.fileUrl)
  }
}
</script>

<style scoped>
.image-area {
  width: 100%;
  height: 400px;
}

.nutrition {
  padding: 20px;
}
</style>