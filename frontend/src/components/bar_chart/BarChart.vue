<script>
  // Importing Bar class from the vue-chartjs wrapper
  import {Bar} from 'vue-chartjs'
  import * as math from 'mathjs'
  // Exporting this so it can be used in other components
  let dataset = [3.3, 3.4, 3.1, 3.7, 3.2, 3.3, 3.1, 3.7, 3.2, 3.3, 3.9, 3.1]
  let avg = math.mean(dataset).toFixed(2)
  export default {
    extends: Bar,
    data() {
      return {
        datacollection: {
          // Data to be represented on x-axis
          labels: ['CS411', 'CS412', 'CS413', 'CS414', 'CS415', 'CS416', 'CS417', 'CS418', 'CS419', 'CS420', 'CS421', 'CS422'],
          datasets: [
            {
              label: 'GPA',
              backgroundColor: '#f87979',
              pointBackgroundColor: 'white',
              borderWidth: 1,
              pointBorderColor: '#249EBF',
              // Data to be represented on y-axis
              data: dataset,
              fill: false
            }
          ]
        },
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
      // renderChart function renders the chart with the datacollection and options object.
      this.renderChart(this.datacollection, this.options)
    }
  }
</script>
