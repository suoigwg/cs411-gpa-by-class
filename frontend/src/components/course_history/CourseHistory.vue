<template>
  <div>
    <div>
      <md-autocomplete
        v-model="selectedCountry"
        :md-options="countries"
        md-layout="box"
        md-dense>
        <label>Type a Course or an Instructor</label>
      </md-autocomplete>
    </div>
    <div class="small" v-if="loaded">
      <LineChart :chart-data="datacollection"></LineChart>
    </div>

  </div>
</template>

<script>
  import lodash from 'lodash'
  import LineChart from '../line_chart/LineChart'

  export default {
    components: {
      LineChart
    },
    data() {
      return {
        course_number: '',
        loaded: true,
        selectedCountry: null,
        selectedEmployee: null,
        countries: [
          'Abdussalam Alawini',
          'CS411'
        ],
        datacollection: {
          labels: ['Spring 2019', 'Spring 2020', 'Spring 2021', 'Spring 2022', 'Spring 2023'],
          datasets: [{
            label: 'GPA',
            data: [1, 2, 3, 4, 5],
            backgroundColor: '#f12121',
            fill: false
          }
          ]
        }
      }
    },
    mounted() {
    },
    watch: {
      course_number: function () {
        this.debouncedGetData()
      }
    },
    created: function () {
      this.debouncedGetData = lodash.debounce(this.getData, 500)
    },
    methods: {
      getData: function () {
        alert('111')
      }
    }
  }
</script>

<style>
  .small {
    max-width: 1000px;
    margin: 10px auto;
    max-height: 50px;
  }

</style>
