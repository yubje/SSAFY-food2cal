<template>
  <div>
    <img class="image-area" :src="fileUrl" alt="s3-image">
    <div class="nutrition">
      <p>치킨</p>
      <p>열량</p>
      <p>탄수화물</p>
      <p>단백질</p>
      <p>지방</p>
    </div>
    <!-- <div class="my-2 d-flex align-center justify-center">
      <v-btn text large color="#F84A0D">Submit</v-btn>
    </div> -->
    <div class="m-0">
      <PostsModal />
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import { mapState } from 'vuex'
import PostsModal from '@/components/common/PostsModal'

export default {
  name: 'Canvas',
  components: {
    PostsModal
  },
  computed: {
    ...mapState(['fileUrl'])
  },
  methods: {
    sendUrl(fileUrl) {
      console.log(fileUrl)
      axios.get('http://8a945e2757a9.ngrok.io/predict/', fileUrl)
        .then((res) => {
          console.log(res)
        })
    },
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