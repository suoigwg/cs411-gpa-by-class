import Vue from 'vue'
import axios from 'axios'
import VueAxios from 'vue-axios'

var API_URL = 'http://localhost:8000'
const ApiService = {
  init() {
    Vue.use(VueAxios, axios)
    Vue.axios.defaults.baseURL = API_URL
  },

  get(url, params = {}) {
    return Vue.axios.get(url, params)
  },

  post(url, params = {}) {
    return Vue.axios.post(url, params)
  },

  put(url, params = {}) {
    return Vue.axios.put(url, params)
  },

  delete(url, params = {}) {
    return Vue.axios.delete(url, params)
  }
}

export default ApiService

export const UserService = {
  login(username, password) {
    return ApiService.post('users/login/', { username: username, password: password })
  },

  register(username, password, isAdmin) {
    console.log(username + ' ' + password + ' ' + isAdmin)
    return ApiService.post('users/register/', { username: username, password: password, isAdmin: isAdmin })
  }
}
