import Vue from 'vue'
import VueRouter from 'vue-router'

import constants from '@/libs/constants'

import Home from '@/views/Home.vue'
// import Camera from '@/views/uploads/Camera'
// import Canvas from '@/views/uploads/Canvas'



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
    component: () => import('@/views/uploads/Camera')
  },
  {
    path: '/canvas',
    name: constants.URL_TYPE.UPLOAD.CANVAS,
    component: () => import('@/views/uploads/Canvas')
  },
  {
    path: '/diary',
    name: constants.URL_TYPE.CALENDAR.DIARY,
    component: () => import('@/views/calendar/Diary')
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
