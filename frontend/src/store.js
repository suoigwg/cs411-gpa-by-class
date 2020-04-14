import Vuex from 'vuex'
import {GET_AVG_GPA_BY_YEAR, GET_COURSE_GPA, GET_SUBJECT_LIST, UPDATE_DEPT_GPA} from './mutation-types'
import {CoursesService, GPAService} from './api.service'
import Vue from 'vue'

Vue.use(Vuex)

export const store = new Vuex.Store({
  state: {
    deptGPA: [],
    subjects: [],
    courseGPA: [],
    annualAvgGPA: [],
  },
  mutations: {
    [UPDATE_DEPT_GPA](state, data) {
      // mutate state
      state.deptGPA = data.sort((a, b) => a['CourseNo'] - b['CourseNo'])
    },
    [GET_SUBJECT_LIST](state, data) {
      state.subjects = data.sort()
    },
    [GET_COURSE_GPA](state, data) {
      state.courseGPA = data.sort((a, b) => (a['Year'] + a['Term']).localeCompare((b['Year'] + b['Term'])))
    },
    [GET_AVG_GPA_BY_YEAR](state, data) {
      state.annualAvgGPA = data.sort((a, b) => (a['Subject'].localeCompare(b['Subject'])))
    }
  },
  actions: {
    fetch_dept_data({commit}, {year, dept}) {
      return GPAService.getGPAByDeptAndYear(year, dept).then((response) => {
        commit(UPDATE_DEPT_GPA, response.data)
      }, () => {
        console.log('fail to load data')
      })
    },
    fetch_subject_list(context) {
      return CoursesService.getSubjects().then((response) => {
        context.commit(GET_SUBJECT_LIST, response.data)
      }, () => {
        console.log('fail to load subjects')
      })
    },
    fetch_course_gpa({commit}, {courseNumber}) {
      return GPAService.getGPAInfo(courseNumber).then((response) => {
        commit(GET_COURSE_GPA, response.data)
      }, () => {
        console.log('fail to load data')
      })
    },
    fetch_annual_avg_gpa({commit}, {year}) {
      return GPAService.getAnnualGPAAvg(year).then((response) => {
        commit(GET_AVG_GPA_BY_YEAR, response.data)
      }, () => {
        console.log('fail to load data')
      })
    }
  }
})

export default {
  state: {
    username: '',
    isAdmin: false,
    loggedIn: false,
    newItems: [],
    updatedItems: [],
    deletedItems: [],
  },

  logIn(username, isAdmin) {
    this.state.username = username
    this.state.isAdmin = isAdmin
    this.state.loggedIn = true
  },

  clearEdit() {
    this.state.newItems = []
    this.state.updatedItems = []
    this.state.deletedItems = []
  },
}

