import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import vuetify from './plugins/vuetify';
import VueCookies from 'vue-cookies'
import axios from 'axios'
import VueCharts from 'vue-chartjs'

Vue.use(VueCookies)

Vue.config.productionTip = false
Vue.prototype.$http = axios;
const csrf = localStorage.getItem("csrftoken")
if (csrf){
  Vue.prototype.$http.defaults.headers.common['X-CSRFToken'] = csrf
}


new Vue({
  router,
  store,
  vuetify,
  VueCharts,
  render: h => h(App)
}).$mount('#app')
