<template>
  <div>
    <div v-if="!comments">
      등록된 댓글이 없습니다.
    </div>
    
    <div class="comment" v-for="comment in comments" :key="`comment_${comment.id}`">
      <!-- <router-link
        class="comment-username" 
        :to="{ name:constants.URL_TYPE.USER.MYPAGE, params:{ id: comment.userid }}"
      >{{ comment.nickname }}</router-link> -->
      <p class="comment-time">{{ comment.updated_at }}</p>
      <p class="comment-time">{{ comment.user.username }}</p>
      <p class="comment-content">{{ comment.content }}</p>
      <!-- <div v-if="checkComment.isComment && comment.commentid === checkComment.commentId">
        <CommentCreate :checkComment="checkComment" @change-comment="updateComment"/>
      </div>
      <div v-else>
        <p class="comment-content">{{ comment.content }}</p>
      </div> -->
      
      <!-- <div class="rightbuttons" v-if="!checkComment.isComment && +commentForm.userid === comment.userid">
        <button class="create-button" style="margin-right:2px;" @click="changeIsComment(comment)">수정</button>
        <button class="create-button" @click="deleteComment(comment.id)">삭제</button>
      </div><br> -->
    </div>
    <hr>
    <!-- <CommentCreate v-if="isLoggedIn" @submit-comment="createComment" /> -->
    <CommentCreate @submit-comment="createComment" />
  </div>
</template>

<script>
import constants from '@/libs/constants.js'
import CommentCreate from './CommentCreate.vue'
// import { mapGetters } from 'vuex'
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
      },
      updateCommentForm: {
        content: '',
        postid: '',
        userid: '',
        commentid: '',
        parentid: '',
        nickname: ''
      }
    }
  },
  computed: {
    // ...mapGetters('userStore', ['isLoggedIn'])
  },
  methods: {
    // changeIsComment(comment) {
    //   this.checkComment.isComment = !this.checkComment.isComment
    //   this.checkComment.commentId  = comment.commentid
    //   this.checkComment.commentValue = comment.content
    //   this.updateCommentForm.postid = comment.postid
    //   this.updateCommentForm.parentid = comment.parentid
    //   this.updateCommentForm.nickname = comment.nickname
    //   this.updateCommentForm.userid = comment.userid
    //   this.updateCommentForm.commentid = comment.commentid
    // },
    getCommentList() {
      this.$http
        .get(process.env.VUE_APP_SERVER_URL + '/posts/' + `${this.postId}` + '/comments/')
        .then(res => {
          console.log(res)
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
    // updateComment(content) {
    //   this.updateCommentForm.content = content
    //   axios.put(`${this.SERVER_URL}/comments/modify`, this.updateCommentForm)
    //     .then(() => {
    //       this.checkComment.isComment = false
    //       this.checkComment.commentId = null
    //       this.checkComment.commentValue = null
    //       this.getCommentList()
    //     })
    //     .catch(err => console.log(err))
    // },
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