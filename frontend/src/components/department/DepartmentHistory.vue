<template>
  <div>
    <div>
      <md-menu md-direction="bottom-end">
        <md-button md-menu-trigger>Select Department</md-button>
        <md-menu-content>
          <md-menu-item @click="setDepartment" v-for="subject in this.$store.state.subjects">{{subject}}</md-menu-item>
        </md-menu-content>
      </md-menu>
    </div>
    <div>
      <input type="range" min="2010" max="2019" step="1" class="slider" v-model.number="year" @change="fetchData">
      <span class="md-subheading">{{year}}</span>
    </div>
    <span class="md-display-3">{{department}}</span>
    <BarChart :chart-data="datacollection"></BarChart>
  </div>
</template>
<script>
  import BarChart from '../bar_chart/BarChart'

  export default {
    data: function () {
      return {
        department: 'BIOE',
        year: 2010,
        datacollection: {
          labels: [],
          datasets: []
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
      this.fetchData()
    },
    methods: {
      fetchData: function () {
        this.$store.dispatch('fetch_dept_data', {year: this.year, dept: this.department}).then(() => {
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
      },
      setDepartment: function (event) {
        this.department = event.target.innerText
        this.fetchData()
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

  .slider {
    -webkit-appearance: none;
    width: 40%;
    height: 5px;
    border-radius: 5px;
    background: #d3d3d3;
    outline: none;
    opacity: 0.7;
    -webkit-transition: .2s;
    transition: opacity .2s;
  }

  .slider::-webkit-slider-thumb {
    -webkit-appearance: none;
    appearance: none;
    width: 25px;
    height: 25px;
    border-radius: 50%;
    background: #4CAF50;
    cursor: pointer;
  }

  .slider::-moz-range-thumb {
    width: 25px;
    height: 25px;
    border-radius: 50%;
    background: #4CAF50;
    cursor: pointer;
  }

</style>
