<template>
  <div>
    <md-field>
      <label>Type in course number here(Example: CS411)</label>
      <md-input v-model="course_number" @keyup.enter.native="fetchData"></md-input>
    </md-field>
    <span class="md-display-3">{{this.title}}</span>
    <div class="small" v-if="loaded">
      <LineChart :chart-data="datacollection"></LineChart>
    </div>
  </div>
</template>

<script>
  import LineChart from '../line_chart/LineChart'

  export default {
    components: {
      LineChart
    },
    data() {
      return {
        course_number: 'cs411',
        loaded: true,
        title: '',
        datacollection: {
          labels: [],
          datasets: []
        }
      }
    },
    created: function () {
      this.fetchData()
    },
    methods: {
      fetchData: function () {
        this.$store.dispatch('fetch_course_gpa', {courseNumber: this.course_number}).then(() => {
          this.datacollection = {
            labels: this.$store.state.courseGPA.map((item) => [item['Term'], item['Year'], item['Name']].join(' ')),
            datasets: [
              {
                label: 'GPA',
                data: this.$store.state.courseGPA.map((item) => item['Value']),
              }
            ]
          }
          if (this.$store.state.courseGPA.length > 0) {
            this.title = this.course_number.toUpperCase() + ' ' + this.$store.state.courseGPA[0]['Title']
          } else {
            this.title = 'No course found'
          }
        })
      }
    },
  }
</script>

<style>
  .small {
    max-width: 1000px;
    margin: 10px auto;
    max-height: 50px;
  }

</style>
