// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import ApiService from './api.service'
import 'bootstrap/dist/css/bootstrap.min.css'
import VueMaterial from 'vue-material'
import 'vue-material/dist/vue-material.min.css'
import 'vue-material/dist/theme/default.css'
import {store} from './store'
import ECharts from 'vue-echarts'

Vue.config.productionTip = false
Vue.use(VueMaterial)
Vue.component('v-chart', ECharts)
ApiService.init()
/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  components: {App},
  template: '<App/>'
})
