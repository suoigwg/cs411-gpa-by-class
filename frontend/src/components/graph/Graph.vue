<template>
  <v-chart :options="polar"/>
</template>

<style>
  /**
   * The default size is 600px×400px, for responsive charts
   * you may need to set percentage values as follows (also
   * don't forget to provide a size for the container).
   */
  .echarts {
    width: 100%;
    height: 100%;
  }
</style>

<script>
  import ECharts from 'vue-echarts'
  import 'echarts/lib/chart/graph'
  import 'echarts/lib/component/polar'

  export default {
    components: {
      'v-chart': ECharts
    },
    data() {
      return {
        polar: {
          polar: {
            center: ['50%', '54%']
          },
          tooltip: {
            trigger: 'axis',
            axisPointer: {
              type: 'cross'
            }
          },
          angleAxis: {
            type: 'value',
            startAngle: 0
          },
          radiusAxis: {
            min: 0
          },
          series: [
            {
              type: 'graph',
              layout: 'none',
              symbolSize: 50,
              roam: true,
              label: {
                show: true
              },
              edgeSymbol: ['circle', 'arrow'],
              edgeSymbolSize: [4, 10],
              edgeLabel: {
                fontSize: 20
              },
              data: [{
                name: 'CS411',
                x: 300,
                y: 300
              }, {
                name: 'CS220',
                x: 800,
                y: 300
              }, {
                name: 'CS598',
                x: 550,
                y: 100
              }, {
                name: 'CS101',
                x: 550,
                y: 500
              }],
              // links: [],
              links: [{
                source: 'CS411',
                target: 'CS220',
              }, {
                source: 'CS598',
                target: 'CS411'
              }, {
                source: 'CS220',
                target: 'CS101'
              },],
              lineStyle: {
                opacity: 0.9,
                width: 2,
                curveness: 0
              }
            }
          ],
          animationDuration: 2000
        }
      }
    }
  }
</script>
