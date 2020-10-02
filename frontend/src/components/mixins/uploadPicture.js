// import constants from '@/libs/constants'
import { mapActions } from 'vuex'

export const uploadPicture = {
  methods: {
    ...mapActions(['upload']),
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
    createName(file) {
      console.log(file)
      const fileName = this.createImageFileName()
      const fileType = file.name.split('.')[1]
      const name = fileName + '.' + fileType
      return name
    },
    handleFileUpload(file) {
      console.log(file.name)
      const fileName = this.createName(file)
      const fileData = {
        file: file,
        name: fileName
      }
      this.upload(fileData)
    },
  }
}