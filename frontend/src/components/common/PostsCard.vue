<template>
  <v-card
    class="mx-auto mt-7"
    max-width="370"
  >
    <v-img
      :src="post.diet_image_path"
      :style="{ backgroundImage: 'url(https://cdn.vuetifyjs.com/images/cards/sunshine.jpg)' }"
      height="200px"
    ></v-img>

    <div class="d-flex align-center justify-space-between">
      <v-card-title>
        <p>{{ post.title }}</p>
        <p class="ml-2 text-subtitle-2">by {{ post.user.username }}</p>
      </v-card-title>

      <div v-if="post.user.username === setName" class="mr-4">
        <button @click.prevent="goUpdatePost(post)"><p class="text-subtitle-2 grey--text">수정</p></button> | 
        <button @click.prevent="deletePost(post)"><p class="text-subtitle-2 grey--text">삭제</p></button>
      </div>
    </div>
    

    <v-card-subtitle>
      {{ post.content }}
    </v-card-subtitle>

    <v-card-actions>
      <v-spacer></v-spacer>

      <v-btn
        icon
        @click="show = !show"
      >
        <!-- <v-icon>{{ show ? 'mdi-chevron-up' : 'mdi-chevron-down' }}</v-icon> -->
        <v-icon>
          mdi-comment
        </v-icon>
      </v-btn>
    </v-card-actions>

    <v-expand-transition>
      <div v-show="show">
        <v-divider></v-divider>
        <Comment :postId="post.id" />
        <!-- <CommentCreate /> -->
      </div>
    </v-expand-transition>
  </v-card>
</template>

<script>
import Comment from '@/components/comment/Comment'
import constants from '@/libs/constants.js'
import SERVER from '@/libs/api'

export default {
  name: 'PostsCard',
  props: {
    post: {
      type: Object
    }
  },
  components: {
    Comment,
    // CommentCreate
  },
  computed: {
    setName() {
      return window.sessionStorage.getItem('username')
    }
  },
  data () {
    return {
      show: false,
    }
  },
  methods: {
    goUpdatePost(post) {
      if (this.setName === post.user.username) {
        this.$router.push({
          name: constants.URL_TYPE.POST.CREATE,
          params: {
            postData: {
              postId: post.id,
              title: post.title,
              content: post.content,
              diet_image_path: post.diet_image_path
            }
          }
        })
        return
      }
      alert('해당 게시글 작성자만 게시글을 수정할 수 있습니다.')
    },
    deletePost(post) {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get(`auth-token`)}`
        }
      }

      if (this.setName === post.user.username) {
        const check = confirm('게시글을 삭제하시겠습니까?')
        if (check) {
          this.$http.delete(process.env.VUE_APP_SERVER_URL + SERVER.ROUTES.createPost + `${post.id}/`, config)
            .then(() => {
              alert('게시글이 삭제되었습니다.')
              this.$router.push({ name: constants.URL_TYPE.POST.DELETE })
            })
        }
        return
      }
      alert('해당 게시글 작성자만 게시글을 삭제할 수 있습니다')
    }
  }
}
</script>