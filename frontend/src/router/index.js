import Vue from 'vue'
import VueRouter from 'vue-router'

import constants from '@/libs/constants'

import Home from '@/views/Home.vue'
import Camera from '@/views/uploads/Camera'



Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/camera',
    name: constants.URL_TYPE.UPLOAD.CAMERA,
    component: Camera
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
