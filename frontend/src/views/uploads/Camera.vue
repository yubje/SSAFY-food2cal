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
    <input v-show="false" ref="inputUpload" type="file" @change="handleFileUpload">

    <video autoplay class="feed"></video>
  
    <button class="snap" @click="takePicture">
      <v-icon dark>mdi-camera</v-icon>
    </button>

    <canvas v-show="false"></canvas>
  </div>
</template>

<script>
import { uploadPicture } from '@/components/mixins/uploadPicture'
import AWS from 'aws-sdk'

export default {
  name: 'Camera',
  data () {
    return {
      file: null,
      fileUrl: null
    }
  },
  methods: {
    init() {
      if ('mediaDevices' in navigator && 'getUserMedia' in navigator.mediaDevices) {
        navigator.mediaDevices.getUserMedia({video: true}).then(stream => {
          const videoPlayer = document.querySelector('video')
          videoPlayer.srcObject = stream;
          videoPlayer.play()
        })
      } else {
        alert('Cannot get Media Devices')
      }
    },
    handleFileUpload() {
      this.file = this.$refs.inputUpload.files[0]
      console.log(this.file)
    },
    dataURItoBlob(dataURI) {
      const binary = atob(dataURI.split(',')[1]);
      const arr = [];
      for (let i = 0; i < binary.length; i++) {
        arr.push(binary.charCodeAt(i));
      }
      return new Blob([new Uint8Array(arr)], {type: 'image/png'})
    },
    upload(name) {
      const s3 = new AWS.S3({
        accessKeyId: process.env.VUE_APP_ACCESS_KEY_ID,
        secretAccessKey: process.env.VUE_APP_SECRECT_ACCESS_KEY,
        region : process.env.VUE_APP_REGION
      })
      const param = {
        'Bucket' : process.env.VUE_APP_BUCKET,
        'Key' : `image/` + name,
        'ACL' : 'public-read',
        'Body' : this.file,
        'ContentType': this.file.type
      }
      s3.upload(param, (err, data) => {
        if(err) {
          console.log('image upload err : ' + err)
          return
        }
        console.log(data)
      })
    },
    takePicture() {
      let ratio = (window.innerHeight < window.innerWidth) ? 16/9: 9/16;
      const picture = document.querySelector('canvas');
      picture.width = (window.innerWidth < 1200) ? window.innerWidth : 1200;
      picture.height = window.innerWidth / ratio;
      const ctx = picture.getContext('2d');
      ctx.imageSmoothingEnabled = true;
      ctx.imageSmoothingQuality = 'high';
      ctx.drawImage(document.querySelector('video'), 0, 0);
      console.log(1)
      const dataUrl = picture.toDataURL('image/png');
      const blobData = this.dataURItoBlob(dataUrl);
      const fileName = this.createImageFileName()
      const file = new File([blobData], fileName + '.png', {type: blobData.type})
      console.log(file)
      this.file = file
      this.upload(this.file.name)
      this.file = null
    }
  },
  mixins: [
    uploadPicture
  ],
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
