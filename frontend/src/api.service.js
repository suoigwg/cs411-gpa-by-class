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
    console.log(url)
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
    return ApiService.post('users/login/', {username: username, password: password})
  },

  register(username, password, isAdmin) {
    return ApiService.post('users/register/', {username: username, password: password, isAdmin: isAdmin})
  }
}

export const CoursesService = {
  getSubjects() {
    return ApiService.get('api/subjects')
  },

  getCourses(subject) {
    return ApiService.get('api/courses', {subject: subject})
  },

  newCourses(courses) {
    return ApiService.post('api/courses/new', {courses: courses})
  },

  updateCourses(courses) {
    return ApiService.post('api/courses/updated', {courses: courses})
  },

  deleteCourses(courses) {
    return ApiService.post('api/courses/deleted', {courses: courses})
  }
}

export const GPAService = {
  getGPAByDeptAndYear(year, dept) {
    return ApiService.get(`gpa/${year}/${dept}`)
  },
  getGPAInfo(subject, number) {
    return ApiService.get('api/coursegpa', {subject: subject, number: number})
  },

  newGPAInfo(gpas) {
    return ApiService.post('api/coursesgpa/new', {gpas: gpas})
  },

  updateGPAInfo(gpas) {
    return ApiService.post('api/coursesgpa/updated', {gpas: gpas})
  },

  deleteGPAInfo(gpas) {
    return ApiService.post('api/coursesgpa/deleted', {gpas: gpas})
  }
}

export const ProfessorService = {
  getProfessorNames() {
    return ApiService.get('api/professorNames')
  },

  getGPA(year, dept) {
    return ApiService.get('api/gpa', {year: year, dept: dept})
  }
}
