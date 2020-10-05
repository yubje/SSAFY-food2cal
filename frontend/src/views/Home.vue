<template>
  <div class="home">
    <div v-show="!isLoading" class="progress-loading">
      <Loading />
    </div>
    
    <div v-for="post in posts" :key="post.id">
      <PostsCard :post="post" />
    </div>
  </div>
</template>

<script>
import PostsCard from '@/components/common/PostsCard'
import Loading from '@/components/common/Loading'
import SERVER from '@/libs/api'
import { mapActions } from 'vuex'

export default {
  name: 'Home',
  data () {
    return {
      posts: null,
      isLoading: true
    }
  },
  components: {
    PostsCard,
    Loading
  },
  methods: {
    ...mapActions([
      'getMonthDiets'
    ]),
    getToday() {
      let time = new Date()
      let year = time.getFullYear()
      let month = time.getMonth() + 1
      month = month >= 10 ? month: '0' + month
      return year + '-' + month
    },
    getPostList() {
      this.isLoading = !this.isLoading
      this.$http
        .get(process.env.VUE_APP_SERVER_URL + SERVER.ROUTES.getPost + '1/')
        .then(res => {
          this.posts = res.data
          this.isLoading = !this.isLoading
        })
        .catch(err => console.log(err.response.data))
    }
  },
  created() {
    this.getPostList()
    const yearMon = this.getToday()
    this.getMonthDiets(yearMon)
  }
}
</script>

<style>
.progress-loading {
  z-index: 10;
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}
</style>
