import Vue from 'vue'
import Vuex from 'vuex'

import AWS from 'aws-sdk'
import axios from 'axios'


Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    fileUrl: null
  },
  mutations: {
    SET_FILE_URL(state, fileUrl) {
      state.fileUrl = fileUrl
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
        // console.log(data.Location)
        commit('SET_FILE_URL', data.Location)
        // return data.Location
        console.log(data.Location)
        axios.post('http://8a945e2757a9.ngrok.io/predict/', data.Location)
          .then((res) => {
            console.log(res)
          })
      })
    }
  },
  modules: {
  }
})
