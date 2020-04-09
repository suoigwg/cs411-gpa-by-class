<script>
  // Importing Bubble class from the vue-chartjs wrapper
  import {Bubble, mixins} from 'vue-chartjs'

  const {reactiveProp} = mixins
  export default {
    extends: Bubble,
    mixins: [reactiveProp],
    data() {
      return {
        options: {
          tooltips: {
            callbacks: {
              label: function (tooltipItem, chartData) {
                return chartData.datasets[0].data[tooltipItem.xLabel]['sub'] + ': ' + tooltipItem.value
              }
            }
          },
          responsive: true,
          maintainAspectRatio: false,
          scales: {
            xAxes: [{
              display: false
            }]
          }
        }
      }
    },
    mounted() {
      this.renderChart(this.chartData, this.options)
    }
  }
</script>
