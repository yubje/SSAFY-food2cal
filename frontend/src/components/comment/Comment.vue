<template>
  <div>
    <!-- <div v-if="!LoginFlag || comments.length" class="my-3 ml-2">
      등록된 댓글이 없습니다.
    </div> -->
    
    <div class="comment" v-for="comment in comments" :key="`comment_${comment.id}`">
      <!-- <router-link
        class="comment-username" 
        :to="{ name:constants.URL_TYPE.USER.MYPAGE, params:{ id: comment.userid }}"
      >{{ comment.nickname }}</router-link> -->
      <div class="d-flex align-center my-2">
        <div class="d-flex">
          <!-- <p class="my-auto">{{ comment.content }}</p> -->
          <!-- <div v-if="checkComment.isComment && comment.comment.user.username === checkComment.commentId"> -->
          <div v-if="checkComment.isComment">
            <CommentCreate :checkComment="checkComment" @change-comment="updateComment"/>
          </div>
          <div v-else class="d-flex">
            <p class="mx-3 my-auto"><strong>{{ comment.user.username }}</strong></p>
            <p class="my-auto">{{ comment.content }}</p>
          </div>
        </div>
        
        
        <v-spacer></v-spacer>
        <!-- <div class="rightbuttons" v-if="!checkComment.isComment && +commentForm.userid === comment.userid"> -->
        <div class="mr-5 my-auto" v-if="!checkComment.isComment && comment.user.username === setName">
          <button @click="changeIsComment(comment)">수정</button>
          <button class="ml-2" @click="deleteComment(comment.id)">삭제</button>
        </div><br>
      </div>
    </div>
    <hr>
    <CommentCreate v-if="LoginFlag" @submit-comment="createComment" />
  </div>
</template>

<script>
import constants from '@/libs/constants.js'
import CommentCreate from './CommentCreate.vue'
import { mapState } from 'vuex'

export default {
  name: 'Comment',
  props: {
    postId: {
      type: Number
    }
  },
  components: {
    CommentCreate
  },
  data() {
    return {
      constants,
      SERVER_URL: process.env.VUE_APP_API_URL,
      comments: null,
      checkComment: {
        isComment: false,
        commentId: null,
        commentValue: null,
        postId: null
      },
      updateCommentForm: {
        content: '',
        postId: null,
        commentId: null,
      }
    }
  },
  computed: {
    ...mapState(['LoginFlag']),
    setName() {
      return window.sessionStorage.getItem('username')
    }
  },
  methods: {
    changeIsComment(comment) {
      this.checkComment.isComment = !this.checkComment.isComment
      this.checkComment.commentId  = comment.id
      this.checkComment.commentValue = comment.content
      this.checkComment.postId = comment.post
    },
    getCommentList() {
      this.$http
        .get(process.env.VUE_APP_SERVER_URL + '/posts/' + `${this.postId}` + '/comments/')
        .then(res => {
          // console.log(res)
          this.comments = res.data
        })
        .catch(err => console.log(err.response.data))
    },
    createComment(content) {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get(`auth-token`)}`
        }
      }

      const commentForm = {
        content: content
      }

      this.$http
        .post(process.env.VUE_APP_SERVER_URL + '/posts/' + `${this.postId}` + '/comments/', commentForm, config)
        .then(() => {
          this.getCommentList()
        })
        .catch(err => console.log(err.response.data))
    },
    updateComment(content) {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get(`auth-token`)}`
        }
      }

      const commentInfo = {
        content: content
      }

      this.$http.put(process.env.VUE_APP_SERVER_URL + '/posts/' + `${this.checkComment.postId}` + '/comments/' + `${this.checkComment.commentId}/`, commentInfo, config)
        .then(() => {
          this.checkComment.isComment = false
          this.checkComment.commentId = null
          this.checkComment.commentValue = null
          this.checkComment.postId = null
          this.getCommentList()
        })
        .catch(err => console.log(err))
    },
    deleteComment(commentId) {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get(`auth-token`)}`
        }
      }

      this.$http
        .delete(process.env.VUE_APP_SERVER_URL + '/comments/' + `${commentId}/`, config)
        .then(() => {
          alert("댓글이 삭제되었습니다.")
          this.getCommentList()
        })
        .catch(err => console.log(err))
    }
  },
  created() {
    this.getCommentList()
  }
}
</script>

<style scoped>

</style>