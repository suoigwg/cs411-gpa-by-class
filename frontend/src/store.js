import Vuex from 'vuex'
import {GET_COURSE_GPA, GET_SUBJECT_LIST, UPDATE_DEPT_GPA} from './mutation-types'
import {CoursesService, GPAService} from './api.service'
import Vue from 'vue'

Vue.use(Vuex)

export const store = new Vuex.Store({
  state: {
    deptGPA: [],
    subjects: [],
    courseGPA: [],
  },
  mutations: {
    [UPDATE_DEPT_GPA](state, data) {
      // mutate state
      state.deptGPA = data.sort((a, b) => a['CourseNo'] - b['CourseNo'])
    },
    [GET_SUBJECT_LIST](state, data) {
      state.subjects = data
    },
    [GET_COURSE_GPA](state, data) {
      state.courseGPA = data.sort((a, b) => (a['Year'] + a['Term']).localeCompare((b['Year'] + b['Term'])))
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
    }
  }
})

export default {
  state: {
    username: 'Chen',
    isAdmin: true,
    loggedIn: true,
    newItems: [],
    updatedItems: [],
    deletedItems: [],
    deptGPA: []
  },

  setDeptGPA(data) {
    this.state.deptGPA = data
  },

  getDeptGPA() {
    return this.state.deptGPA
  },

  clearEdit() {
    this.state.newItems = []
    this.state.updatedItems = []
    this.state.deletedItems = []
  }
}

