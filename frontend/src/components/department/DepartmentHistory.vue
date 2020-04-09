<template>
  <div>
    <div>
      <md-menu md-direction="bottom-end">
        <md-button md-menu-trigger>Select Department</md-button>
        <md-menu-content>
          <md-menu-item @click="setDepartment" v-for="subject in this.$store.state.subjects">{{subject}}</md-menu-item>
        </md-menu-content>
      </md-menu>
      <span class="subject">{{department}}</span>
    </div>
    <BarChart :chart-data="datacollection"></BarChart>
  </div>
</template>
<script>
  import BarChart from '../bar_chart/BarChart'
  import {UPDATE_DEPT_GPA} from '../../mutation-types'
  import {GPAService} from '../../api.service'
  import store from '../../store'
  import {mapState} from 'vuex'

  export default {
    data: function () {
      return {
        department: '',
        grade: [],
        datacollection: {
          // labels: ['CS411', 'CS412', 'CS413', 'CS414', 'CS415', 'CS416', 'CS417', 'CS418', 'CS419', 'CS420', 'CS421', 'CS422'],
          // labels: this.deptGPA.map((item) => item['Subject'] + item['CourseNo']),
          // datasets: [
          //   {
          //     label: 'GPA',
          //     backgroundColor: '#f87979',
          //     pointBackgroundColor: 'white',
          //     borderWidth: 1,
          //     pointBorderColor: '#249EBF',
          //     // Data to be represented on y-axis
          //     data: this.deptGPA.map((item) => item['Value']),
          //     fill: false
          //   },
          // ]
        }
      }
    },
    components: {
      BarChart
    },
    mounted() {
    },
    created() {
      if (this.$store.state.subjects.length === 0) {
        this.$store.dispatch('fetch_subject_list')
      }
    },
    methods: {
      setDepartment: function (event) {
        this.department = event.target.innerText
        this.$store.dispatch('fetch_dept_data', {year: 2010, dept: this.department}).then(() => {
          this.datacollection = {
            labels: this.$store.state.deptGPA.map((item) => [item['Subject'], item['CourseNo']].join(' ')),
            datasets: [
              {
                label: 'GPA',
                data: this.$store.state.deptGPA.map((item) => item['Value']),
                backgroundColor: '#448aff',
              }
            ]
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
    max-height: 150px;
  }

  .subject {
    display: inline-block;
    vertical-align: middle;
  }

</style>
