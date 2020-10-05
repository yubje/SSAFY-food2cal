<template>
  <div class="home">
    <div v-for="post in posts" :key="post.id">
      <PostsCard :post="post" />
    </div>
  </div>
</template>

<script>
import PostsCard from '@/components/common/PostsCard'
import SERVER from '@/libs/api'

export default {
  name: 'Home',
  data () {
    return {
      posts: null
    }
  },
  components: {
    PostsCard
  },
  methods: {
    getPostList() {
      this.$http
        .get(process.env.VUE_APP_SERVER_URL + SERVER.ROUTES.getPost + '1/')
        .then(res => {
          this.posts = res.data
          console.log(res.data)
        })
        .catch(err => console.log(err.response.data))
    }
  },
  created() {
    this.getPostList()
  }
}
</script>
