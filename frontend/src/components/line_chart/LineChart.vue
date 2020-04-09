<script>
  // Importing Line class from the vue-chartjs wrapper
  import {Line, mixins} from 'vue-chartjs'
  // eslint-disable-next-line no-unused-vars

  const {reactiveProp} = mixins
  export default {
    extends: Line,
    mixins: [reactiveProp],
    data() {
      return {
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

          // annotation: {
          //   events: ['click'],
          //   annotations: [
          //     {
          //       drawTime: 'afterDraw',
          //       id: 'hline',
          //       type: 'line',
          //       mode: 'horizontal',
          //       scaleID: 'y-axis-0',
          //       value: avg,
          //       borderColor: 'black',
          //       borderWidth: 1,
          //       borderDash: [2, 2],
          //       label: {
          //         // backgroundColor: 'red',
          //         content: 'Average ' + avg,
          //         enabled: true
          //       }
          //     }
          //   ]
          // }
        }
      }
    },
    mounted() {
      // renderChart function renders the chart with the dataCollection and options object.
      this.renderChart(this.chartData, this.options)
    },
    options: {}
  }
</script>
