import Vue from 'vue'
import Vuex from 'vuex'

import AWS from 'aws-sdk'
// import constants from '@/libs/constants'
import SERVER from '@/libs/api'
import axios from 'axios'


Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    fileUrl: null,
    foodInfo: []
  },
  mutations: {
    SET_FILE_URL(state, fileUrl) {
      state.fileUrl = fileUrl
    },
    SET_FOOD_INFO(state, foodInfo) {
      state.foodInfo = foodInfo
    }
  },
  actions: {
    upload({ commit }, fileData) {
      const s3 = new AWS.S3({
        accessKeyId: process.env.VUE_APP_ACCESS_KEY_ID,
        secretAccessKey: process.env.VUE_APP_SECRECT_ACCESS_KEY,
        region : process.env.VUE_APP_REGION
      })
      const param = {
        'Bucket' : process.env.VUE_APP_BUCKET,
        'Key' : `image/` + fileData.name,
        'ACL' : 'public-read',
        'Body' : fileData.file,
        'ContentType': fileData.file.type
      }
      s3.upload(param, (err, data) => {
        if(err) {
          console.log('image upload err : ' + err)
          return
        }
        commit('SET_FILE_URL', data.Location)
        console.log(data.Location)
        axios.post(process.env.VUE_APP_SERVER_URL + SERVER.ROUTES.predict, data.Location)
          .then((res) => {
            commit('SET_FOOD_INFO', res.data)
            console.log(res.data)
          })
          .catch(err => console.log(err))
          // .then(() => {
          //   this.$router.push({ name: constants.URL_TYPE.UPLOAD.CANVAS })
          // })
      })
    }
  },
  modules: {
  }
})
