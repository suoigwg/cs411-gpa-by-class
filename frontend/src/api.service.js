import Vue from 'vue'
import axios from 'axios'
import VueAxios from 'vue-axios'

var API_URL = 'http://3.83.67.228:8000'
var MONGO_URL = 'http://3.83.67.228:8001'
const ApiService = {
  init() {
    Vue.use(VueAxios, axios)
    Vue.axios.defaults.baseURL = API_URL
  },

  get(url, params = {}) {
    console.log(url)
    return Vue.axios.get(url, {params: params})
  },

  post(url, params = {}) {
    console.log(url)
    return Vue.axios.post(url, params)
  },

  put(url, params = {}) {
    console.log(url)
    return Vue.axios.put(url, params)
  },

  delete(url, params = {}) {
    console.log(url)
    return Vue.axios.delete(url, params)
  },

  getMongo(url, params = {}) {
    console.log(url, params)
    return Vue.axios.get(url, {params, baseURL: MONGO_URL})
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
    return ApiService.get('api/subjects/')
  },

  getCourses(subject) {
    return ApiService.get('api/courses/', {subject: subject})
  },

  newCourses(courses) {
    return ApiService.post('api/courses/new/', {courses: courses})
  },

  updateCourses(courses) {
    return ApiService.post('api/courses/updated/', {courses: courses})
  },

  deleteCourses(courses) {
    return ApiService.post('api/courses/deleted/', {courses: courses})
  },

  getPrerequisite(course) {
    return ApiService.getMongo("api/courseprereq/", {course: course})
  }
}

export const GPAService = {
  getAnnualGPAAvg(year) {
    return ApiService.get(`gpa/avg/${year}`)
  },
  getGPAByDeptAndYear(year, dept) {
    return ApiService.get(`gpa/${year}/${dept}`)
  },
  getGPAInfo(courseNumber) {
    return ApiService.get(`gpa/${courseNumber}`)
  },
  getCourseGPAInfo(subject, courseno) {
    return ApiService.get('api/coursegpa/', {subject: subject, number: courseno})
  },
  newGPAInfo(gpas) {
    return ApiService.post('api/coursesgpa/new/', {gpas: gpas})
  },

  updateGPAInfo(gpas) {
    return ApiService.post('api/coursesgpa/updated/', {gpas: gpas})
  },

  deleteGPAInfo(gpas) {
    return ApiService.post('api/coursesgpa/deleted/', {gpas: gpas})
  },

  getInstructorGrading(name) {
    return ApiService.get('gpa/instructor/' + name)
  }


}

export const ProfessorService = {
  getProfessorNames() {
    return ApiService.get('api/professorNames/')
  },

  getGPA(year, dept) {
    return ApiService.get('api/gpa/', {year: year, dept: dept})
  },

  searchProf(prefix) {
    return ApiService.get('api/prof/' + prefix)
  }
}

export const AdvancedQueryService = {
  execute(subject) {
    return ApiService.get('api/avggpa/', {subject: subject})
  }
}
