<script>
  // Importing Bar class from the vue-chartjs wrapper
  import {Bar, mixins} from 'vue-chartjs'

  const {reactiveProp} = mixins
  import * as math from 'mathjs'
  import store from '../../store'
  // Exporting this so it can be used in other components
  let avg = 0.0
  export default {
    extends: Bar,
    mixins: [reactiveProp],
    data() {
      return {
        gpaData: [],
        // Chart.js options that controls the appearance of the chart
        options: {
          scales: {
            yAxes: [{
              ticks: {
                beginAtZero: true
              },
              gridLines: {
                display: true
              }
            }],
            xAxes: [{
              gridLines: {
                display: false
              }
            }]
          },
          legend: {
            display: true
          },
          responsive: true,
          maintainAspectRatio: false,
          annotation: {
            events: ['click'],
            annotations: [
              {
                drawTime: 'afterDraw',
                id: 'hline',
                type: 'line',
                mode: 'horizontal',
                scaleID: 'y-axis-0',
                value: avg,
                borderColor: 'black',
                borderWidth: 1,
                borderDash: [2, 2],
                label: {
                  // backgroundColor: 'red',
                  content: 'Average ' + avg,
                  enabled: true
                }
              }
            ]
          }
        }
      }
    },
    mounted() {
      this.renderChart(this.chartData, this.options)
    },
  }
</script>
