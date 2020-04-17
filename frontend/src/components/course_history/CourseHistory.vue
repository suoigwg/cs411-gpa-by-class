<template>
  <div>
    <md-autocomplete v-model="keyword" :md-options="instructors" @md-changed="getInstructors"
                     @md-closed="fetchData" @keyup.enter.native="fetchData">
      <label>Type in course number or Instructor name here</label>
      <template slot="md-autocomplete-item" slot-scope="{ item }">{{ item}}</template>
    </md-autocomplete>
    <span class="md-display-3">{{this.title}}</span>
    <div class="small" v-if="loaded">
      <LineChart :chart-data="datacollection"></LineChart>
    </div>
  </div>
</template>

<script>
  import LineChart from '../line_chart/LineChart'
  import {ProfessorService} from '../../api.service'

  export default {
    components: {
      LineChart
    },
    data() {
      return {
        keyword: 'cs411',
        loaded: true,
        title: '',
        datacollection: {
          labels: [],
          datasets: []
        },
        instructors: []
      }
    },
    created: function () {
      this.fetchData()
    },
    methods: {
      fetchData: function () {
        const isDigit = n => /\d+/.test(n)
        let findInstructor = true
        for (let i = 0; i < this.keyword.length; i++) {
          if (isDigit(this.keyword[i])) {
            findInstructor = false
          }
        }
        let type = findInstructor ? 'fetch_instructor_grading' : 'fetch_course_gpa'
        console.log('type' + type)
        this.$store.dispatch(type, {courseNumber: this.keyword}).then(() => {
          this.datacollection = {
            labels: this.$store.state.courseGPA.map((item) => [item['Term'], item['Year'], findInstructor ? item['Title'] : item['Name']].join(' ')),
            datasets: [
              {
                label: 'GPA',
                data: this.$store.state.courseGPA.map((item) => item['Value']),
              }
            ]
          }
          if (this.$store.state.courseGPA.length > 0) {
            this.title = this.keyword.toUpperCase() + ' ' + (findInstructor ? '' : this.$store.state.courseGPA[0]['Title'])
          } else {
            this.title = 'No course found'
          }
        })
      },
      getInstructors(searchTerm) {
        this.instructors = new Promise(resolve => {
          window.setTimeout(() => {
            if (!searchTerm || searchTerm.length < 3) {
              resolve(this.instructors)
            } else {
              const term = searchTerm.toLowerCase()
              return ProfessorService.searchProf(term).then((response) => resolve(response['data']))
            }
          }, 500)
        })
      }
    },
  }
</script>

<style>
  .small {
    margin: 10px auto;
  }

</style>
