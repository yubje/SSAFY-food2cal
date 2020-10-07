import Vue from 'vue'
import Vuex from 'vuex'

import AWS from 'aws-sdk'
// import constants from '@/libs/constants'
import SERVER from '@/libs/api'
import axios from 'axios'

import cookies from 'vue-cookies'
import router from '../router'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    fileUrl: null,
    dietMonthInfo: null,
    foodInfo: [],
    LoginFlag: false,
    standard: null,
    authToken: cookies.get('auth-token')
  },
  mutations: {
    SET_FILE_URL(state, fileUrl) {
      state.fileUrl = fileUrl
    },
    SET_FOOD_INFO(state, foodInfo) {
      state.foodInfo = foodInfo
    },
    SET_DIET_INFO(state, dietMonthInfo) {
      state.dietMonthInfo = dietMonthInfo
    },
    SET_LOGIN_FLAG(state) {
      state.LoginFlag = !!state.authToken
    },
    LOGIN_STATE(state, result) {
      if ( result === true) {
        state.LoginFlag = result
      } else {
        state.LoginFlag = false
        state.authToken = null
      }
    },
    SET_STANDARD(state) {
      if (state.LoginFlag === true) {
        console.log('hi')
      }
    },
    SET_TOKEN(state, token) {
      state.authToken = token
      cookies.set('auth-token', token)
    },
    DELETE_TOKEN(state) {
      state.authToken = null
      cookies.remove('auth-token')
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
      })
    },
    getMonthDiets({ commit }, yearMon) {
      const config = {
        headers: {
          Authorization: `Token ${cookies.get(`auth-token`)}`
        }
      }
      
      // const date = title.split(' ')
      // let year = +date[1]
      // let month = +date[0].slice(0, -1)
      // month = month >= 10 ? month: '0' + month
      // const yearMon = year + '-' + month
      // console.log(yearMon)
      window.localStorage.setItem('yearMon', yearMon);

      axios.get(process.env.VUE_APP_SERVER_URL + SERVER.ROUTES.diets + `${yearMon}/`, config)
        .then(res => {
          commit('SET_DIET_INFO', res.data)
          // this.dietMonthInfo = res.data
          // console.log(res.data)
        })
        .catch(err => {
          console.log(err)
        })
    },
    loginTry({ state, commit }, LoginData) {
      if (state.LoginFlag === false) {
        if (LoginData.username.trim() && LoginData.password.trim()) {
          axios
            .post(process.env.VUE_APP_SERVER_URL + '/users/login/', LoginData, { headers: { 'X-CSRFToken': cookies.get('csrftoken')}})
            .then(res => {
              const token = res.data.key
              cookies.set('auth-token', token)
              commit("SET_TOKEN", token)
              commit("LOGIN_STATE", true)
              router
                .push({ name: 'Home'})
                .catch(err => {
                  if(err.name != "NavigationDuplicated" ){
                    throw err
                  }
                })
            })
            .catch(err => {
              commit("LOGIN_STATE", false)
              console.log(err)
            })
          
        }
      } else {
        router.push({ name: 'Home'})
        alert('이미 로그인 상태입니다.')
      }
    },
    logoutTry({ state, getters, commit }) {
      if (getters.LoginFlag === true) {
        const config = {
          headers: {'Authorization': `Token ${state.authToken}`}
        }
        axios
          .post(process.env.VUE_APP_SERVER_URL + '/users/logout/', null, config)
          .catch(err=>console.log(err.response))
          .finally(() => {
            window.sessionStorage.removeItem('username')
            cookies.remove('auth-token')
            commit("LOGIN_STATE", false)
            router.push({ name:'Home'})
          })
      }
    },
    getProfile() {
      console.log('try getprofile')
      const config = {
        headers: {
          Authorization: `Token ${cookies.get(`auth-token`)}`
        }
      }
      axios
        .get(process.env.VUE_APP_SERVER_URL + '/users/profiles/', config)
        .then(res => {
          console.log(res.data)
          window.sessionStorage.setItem('username', res.data[0].user)
          window.sessionStorage.setItem('standard', res.data[0].standard)
        })
        .catch(err => console.log(err))
    }
  },
  getters: {
    LoginFlag: state => !!state.authToken
  },


  modules: {
  }
})
