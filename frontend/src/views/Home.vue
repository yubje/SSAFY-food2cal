<template>
  <div class="home">
    <div v-for="post in posts" :key="post.id">
      <PostsCard :post="post" />
    </div>
    <v-btn
      @click="test()"
    >
    다이어트 통계 데이터
    </v-btn>
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
    },
    test() {
      this.$http
        .get(process.env.VUE_APP_SERVER_URL + '/diets/diet_statistics/', 
            { headers: {  'X-CSRFToken': this.$cookies.get('csrftoken'),
                          'Authorization': `Token ${this.$cookies.get('auth-token')}`
        }})
        .then(res => {
          console.log(res)
        })
    }
  },
  created() {
    this.getPostList()
  }
}
</script>
