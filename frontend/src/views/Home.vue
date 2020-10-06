<template>
  <div class="home">
    <div v-show="!isLoading" class="progress-loading">
      <Loading />
    </div>
    
    <div v-for="post in posts" :key="post.id">
      <PostsCard :post="post" />
    </div>
    <infinite-loading @infinite="infiniteHandler" spinner="circles"></infinite-loading>
  </div>
</template>

<script>
import PostsCard from '@/components/common/PostsCard'
import Loading from '@/components/common/Loading'
import InfiniteLoading from 'vue-infinite-loading'
import SERVER from '@/libs/api'
import { mapActions } from 'vuex'

export default {
  name: 'Home',
  data () {
    return {
      posts: null,
      isLoading: true,
      limit: 0,
    }
  },
  components: {
    PostsCard,
    Loading,
    InfiniteLoading
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
    infiniteHandler($state) {
      this.$http
        .get(process.env.VUE_APP_SERVER_URL + SERVER.ROUTES.getPost + `${this.limit+1}/`)
        .then(res => {
          setTimeout(() => {
            if (res.data.length) {
              this.posts = this.posts.concat(res.data)
              $state.loaded()
              this.limit += 1
              if (this.posts.length / 10 === 0) {
                $state.complete()
              }
            } else {
              $state.complete()
            }
          }, 1000)
        })
        .catch(err => console.log(err.response.data))
    },
  },
  created() {
    this.$http.get(process.env.VUE_APP_SERVER_URL + SERVER.ROUTES.getPost + `${this.limit}/`)
      .then(res => {
        this.posts = res.data
      })
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
