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
  </div>
</template>

<script>
import { mapState } from 'vuex'

export default {
  name: 'Canvas',
  computed: {
    ...mapState(['fileUrl'])
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
  margin-bottom: 3rem;
}
</style>