<template>
  <div class="home">
    <!-- <div v-for="post in posts" :key="post.id">
      <PostsCard :post="post" />
    </div> -->
    <PostsCard />
  </div>
</template>

<script>
import PostsCard from '@/components/common/PostsCard'

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
        .get(process.env.VUE_APP_SERVER_URL + 'posts/pages/1/')
        .then(res => {
          this.posts = res.data
          console.log(res.data)
        })
        .catch(err => console.log(err.response.data))
    }
  },
  created() {
    // this.getPostList()
  }
}
</script>
