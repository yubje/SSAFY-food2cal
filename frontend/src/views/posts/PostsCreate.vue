<template>
  <div class="d-flex justify-center flex-column">
    <div v-if="checkBefore" class="pt-7 d-flex justify-center align-center">
      <p class="mb-0 camera-content">파일을 업로드해주세요</p>
      <v-icon
        @click="$refs.inputUpload.click()"
        class="ml-2"
      >
        mdi-upload
      </v-icon>
    </div>
    <input v-show="false" ref="inputUpload" type="file" @change="uploadFile">

    <div v-if="!checkBefore">
      <img class="image-area" :src="fileUrl" alt="s3-image">
    </div>
    <v-col cols="12" sm="6" md="4">
      <v-text-field 
        label="Title*" 
        required 
        v-model="title"
      ></v-text-field>
    </v-col>
    <v-col cols="12" sm="6" md="12">
      <v-textarea
        clearable
        clear-icon="mdi-close-circle"
        label="Content*"
        v-model="content"
      ></v-textarea>
    </v-col>
    <v-btn
      color="#F84A0D"
      text
      large
    >
      Submit
    </v-btn>
  </div>
</template>

<script>
import SERVER from '@/libs/api'
import { mapState } from 'vuex'
import { uploadPicture } from '@/components/mixins/uploadPicture'

export default {
  name: 'PostsCreate',
  data () {
    return {
      title: null,
      content: null,
      checkBefore: 1
    }
  },
  created () {
    this.checkBefore = +this.$route.params.id
  },
  computed: {
    ...mapState([
      'fileUrl',
      'foodInfo'
    ])
  },
  methods: {
    uploadFile() {
      this.handleFileUpload(this.$refs.inputUpload.files[0])
      this.checkBefore = 0
    },
    createPost() {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get(`auth-token`)}`
        }
      }

      const postData = {
        title: this.title,
        content: this.content,
        diet_image_path: this.fileUrl
      }

      this.$http.post(process.env.VUE_APP_SERVER_URL + SERVER.ROUTES.createPost, postData, config)
        .then(res => {
          console.log(res)
        })
        .catch(err => {
          console.log(err)
        })
    }
  },
  mixins: [
    uploadPicture
  ]
}
</script>

<style scoped>
.image-area {
  width: 100%;
  height: 400px;
}
</style>