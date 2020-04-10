<template>
  <div>
    <div>
      <input type="range" min="2010" max="2019" step="1" class="slider" v-model.number="year" @change="fetchData">
      <span class="md-subheading">{{year}}</span>
    </div>
    <BubbleChart :chart-data="this.datacollection"></BubbleChart>
  </div>
</template>

<script>
  import BubbleChart from '../bubble_chart/BubbleChart'

  export default {
    name: 'AllGrades',
    data: () => ({
      year: 2019,
      datacollection: {
        labels: [],
        datasets: []
      }
    }),
    components: {
      BubbleChart
    },
    created() {
      this.fetchData()
    },
    methods: {
      fetchData: function () {
        this.$store.dispatch('fetch_annual_avg_gpa', {year: this.year}).then(() => {
          let bubble = []
          this.$store.state.annualAvgGPA.forEach((record, id) => {
            bubble.push({
              x: id,
              y: record['Average'],
              r: record['Average'] / 4.0 * 15,
              sub: record['Subject']
            })
          })
          this.datacollection = {
            labels: this.$store.state.annualAvgGPA.map((item) => item['Subject']),
            datasets: [
              {
                label: 'GPA',
                data: bubble,
                backgroundColor: '#448aff',
              }
            ]
          }
          console.log(bubble)
        })
      }
    }
  }
</script>

<style scoped>
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
