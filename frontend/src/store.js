import Vuex from 'vuex'
import {UPDATE_DEPT_GPA, GET_SUBJECT_LIST} from './mutation-types'
import ApiService, {GPAService, CoursesService} from './api.service'
import Vue from 'vue'

Vue.use(Vuex)

export const store = new Vuex.Store({
  state: {
    deptGPA: [],
    subjects: []
  },
  mutations: {
    [UPDATE_DEPT_GPA](state, data) {
      // mutate state
      state.deptGPA = data.sort((a, b) => a['CourseNo'] - b['CourseNo'])
    },
    [GET_SUBJECT_LIST](state, data) {
      state.subjects = data
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
      CoursesService.getSubjects().then((response) => {
        context.commit(GET_SUBJECT_LIST, response.data)
      }, () => {
        console.log('fail to load subjects')
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

