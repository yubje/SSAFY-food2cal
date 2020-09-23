// import AWS from 'aws-sdk'

export const uploadPicture = {
  methods: {
    createImageFileName() {
      let time = new Date()
      let year = time.getFullYear().toString()
      let month = (time.getMonth() + 1).toString()
      let date = time.getDate().toString()
      let day = time.getDay().toString()
      let hours = time.getHours().toString()
      let minutes = time.getMinutes().toString()
      let seconds = time.getSeconds().toString()
      let milliseconds = time.getMilliseconds().toString()
      return year+month+date+day+hours+minutes+seconds+milliseconds
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
    // }
  }
}