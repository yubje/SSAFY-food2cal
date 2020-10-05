<template>
  <div class="camera">
    <div class="pt-7 d-flex justify-center">
      <p class="camera-content">사진을 촬영하거나 파일을 업로드해주세요</p>
      <v-icon
        dark
        @click="$refs.inputUpload.click()"
        class="ml-2"
      >
        mdi-upload
      </v-icon>
    </div>
    <input v-show="false" ref="inputUpload" type="file" @change="uploadFile">

    <video autoplay class="feed"></video>
  
    <button class="snap" @click="takePicture">
      <v-icon dark>mdi-camera</v-icon>
    </button>

    <canvas v-show="false"></canvas>
  </div>
</template>

<script>
import constants from '@/libs/constants'
import { uploadPicture } from '@/components/mixins/uploadPicture'
import { mapActions } from 'vuex'
// import AWS from 'aws-sdk'

export default {
  name: 'Camera',
  data () {
    return {
      constants,
      file: null,
      fileUrl: null
    }
  },
  computed: {
  },
  methods: {
    ...mapActions(['upload']),
    init() {
      if ('mediaDevices' in navigator && 'getUserMedia' in navigator.mediaDevices) {
        navigator.mediaDevices.getUserMedia({video: true})
          .then(stream => {
            const videoPlayer = document.querySelector('video')
            videoPlayer.srcObject = stream;
            videoPlayer.play()
          })
          .catch(err => {console.log(err)})
      } else {
        alert('Cannot get Media Devices')
      }
    },
    // createName() {
    //   const fileName = this.createImageFileName()
    //   const fileType = this.file.name.split('.')[1]
    //   const name = fileName + '.' + fileType
    //   return name      
    // },
    // handleFileUpload() {
    //   this.file = this.$refs.inputUpload.files[0]
    //   const fileName = this.createName()
    //   const fileData = {
    //     file: this.file,
    //     name: fileName
    //   }
    //   this.upload(fileData)
    //   this.file = null
    // },
    goToCanvas() {
      if (this.$route.query.date) {
        this.$router.push({ name: constants.URL_TYPE.UPLOAD.CANVAS, query: { date: this.$route.query.date, type: this.$route.query.type } })
      } else {
        this.$router.push({ name: constants.URL_TYPE.UPLOAD.CANVAS })
      }
    },
    async uploadFile() {
      await this.handleFileUpload(this.$refs.inputUpload.files[0])
      await this.goToCanvas()
    },
    dataURItoBlob(dataURI) {
      const binary = atob(dataURI.split(',')[1]);
      const arr = [];
      for (let i = 0; i < binary.length; i++) {
        arr.push(binary.charCodeAt(i));
      }
      return new Blob([new Uint8Array(arr)], {type: 'image/png'})
    },
    // upload(name) {
    //   const s3 = new AWS.S3({
    //     accessKeyId: process.env.VUE_APP_ACCESS_KEY_ID,
    //     secretAccessKey: process.env.VUE_APP_SECRECT_ACCESS_KEY,
    //     region : process.env.VUE_APP_REGION
    //   })
    //   const param = {
    //     'Bucket' : process.env.VUE_APP_BUCKET,
    //     'Key' : `image/` + name,
    //     'ACL' : 'public-read',
    //     'Body' : this.file,
    //     'ContentType': this.file.type
    //   }
    //   s3.upload(param, (err, data) => {
    //     if(err) {
    //       console.log('image upload err : ' + err)
    //       return
    //     }
    //     console.log(data)
    //   })
    // },
    async takePicture() {
      // let ratio = (window.innerHeight < window.innerWidth) ? 16/9: 9/16;
      const picture = document.querySelector('canvas')
      // picture.width = (window.innerWidth < 1200) ? window.innerWidth : 1200;
      picture.width = 414
      picture.height = 408
      // console.log(document.querySelector('video'))
      // picture.height = window.innerWidth / ratio;
      const ctx = picture.getContext('2d')
      ctx.imageSmoothingEnabled = true
      ctx.imageSmoothingQuality = 'high'
      ctx.drawImage(document.querySelector('video'), 0, 0, 414, 350)
      const dataUrl = picture.toDataURL('image/png')
      const blobData = this.dataURItoBlob(dataUrl);
      const fileName = this.createImageFileName()
      const file = new File([blobData], fileName + '.png', { type: blobData.type })
      this.file = file
      const fileData = {
        file: this.file,
        name: this.file.name
      }
      await this.upload(fileData)
      await this.goToCanvas()
    }
  },
  mixins: [
    uploadPicture
  ],
  created() {
  },
  beforeMount() {
    this.init()
  }
}
</script>

<style lang="scss" scoped>
.camera {
  z-index: 1;
  width: 100vw;
  height: 100%;
  background-color: #000;

  .feed {
    display: block;
    overflow: hidden;
    width: 100%;
    max-width: 1200px;
    height: 60%;
    // padding: 25px;
    box-sizing: border-box;
    margin: 0 auto;
    background-color: #000;
  }

  .snap {
    display: block;
    width: 75px;
    height: 75px;
    border-radius: 50%;

    margin: 10px auto 0;

    background-color: transparentize($color: #FF890E, $amount: 0.75);
    border: 1px solid #000;
    outline: none;

    cursor: pointer;

    &:hover {
      background-color: #FF890E;
    }
    &:active {
      background-color: darken($color: #FF890E, $amount: .10);
    }
  }

  .camera-content {
    color: #fff;
    text-align: center;
    padding-top: 1rem;
  }
}
</style>
