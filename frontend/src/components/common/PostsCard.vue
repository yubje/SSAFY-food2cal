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

    <v-card-title>
      {{ post.title }} by {{ post.user.username }}
    </v-card-title>

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
// import CommentCreate from '@/components/comment/CommentCreate'

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
  data () {
    return {
      show: false,
      // commentForm: {
      //   content: ''
      // },
    }
  },
  methods: {
    
  }
}
</script>