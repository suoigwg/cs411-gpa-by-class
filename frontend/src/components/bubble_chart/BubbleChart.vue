<script>
  // Importing Bubble class from the vue-chartjs wrapper
  import {Bubble} from 'vue-chartjs'
  // Exporting this so it can be used in other components
  let mockData = [
    {
      x: 11,
      y: 3.1,
      r: 10
    },
    {
      x: 60,
      y: 3.2,
      r: 20
    },
    {
      x: 40,
      y: 3.3,
      r: 25
    },
    {
      x: 80,
      y: 3.3,
      r: 50
    },
    {
      x: 20,
      y: 4.0,
      r: 25
    },
    {
      x: 0,
      y: 3.8,
      r: 5
    }
  ]
  export default {
    extends: Bubble,
    data() {
      return {
        datacollection: {
          // Data to be represented on x-axis
          labels: ['Data'],
          datasets: [
            {
              label: 'Course',
              backgroundColor: '#f87979',
              pointBackgroundColor: 'white',
              borderWidth: 1,
              pointBorderColor: '#249EBF',
              // Data to be represented on y-axis
              data: mockData
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
              },
              ticks: {
                callback: function (value, index, values) {
                  return 'CS4' + value
                }
              }
            }]
          },
          legend: {
            display: true
          },
          responsive: true,
          maintainAspectRatio: false
        }
      }
    },
    mounted() {
      // renderChart function renders the chart with the datacollection and options object.
      this.renderChart(this.datacollection, this.options)
    }
  }
</script>
