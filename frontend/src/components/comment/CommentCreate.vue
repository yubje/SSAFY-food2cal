<template>
  <div>
    <span v-if="checkComment">
      <input @keypress.enter.prevent="changeInput" :value="checkComment.commentValue" @input="newValue=$event.target.value">
      <button class="ml-5" @click.prevent="changeInput" type="submit">수정</button>
    </span>
    <span v-else>
      <input @keypress.enter.prevent="onInput" v-model="commentValue" placeholder="댓글을 입력해주세요">
      <button class="ml-3" @click.prevent="onInput" type="submit">제출</button>
    </span>
  </div>
</template>

<script>
export default {
  name: 'CreateComment',
  data() {
    return {
      commentValue: '',
      newValue: ''
    }
  },
  props: {
    checkComment: {
      type: Object
    }
  },
  methods: {
    onInput() {
      this.$emit('submit-comment', this.commentValue)
      this.commentValue = null
    },
    changeInput() {
      this.$emit('change-comment', this.newValue)
    }
  }
}
</script>

<style scoped>
.comment-input {
  display: flex;
}

input {
  padding: 3px;
  margin: 10px auto;
  width: 85%;
  border: 1px solid #000;
  border-radius: 5px;
}

.create-button {
  border: none;
  cursor: pointer;
  color: black;
  margin: 0 10px;
  /* width: 15%; */
}
</style>