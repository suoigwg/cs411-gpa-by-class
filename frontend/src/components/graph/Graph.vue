<template>
  <div class="wrapper">
    <md-field>
      <label>Course Number</label>
      <md-input @keyup.enter.native="fetchData" v-model="courseNumber"></md-input>
    </md-field>
    <v-chart :options="polar"/>
  </div>
</template>


<script>
  import ECharts from 'vue-echarts'
  import 'echarts/lib/chart/graph'
  import 'echarts/lib/component/polar'
  import 'echarts/lib/component/tooltip'
  import {CoursesService} from '../../api.service'

  export default {
    components: {
      'v-chart': ECharts,
    },
    data() {
      return {
        'courseNumber': 'cs418',
        polar: {}
      }
    },
    mounted() {
      this.fetchData()
    },
    methods: {
      fetchData: function () {
        const isDigit = n => /\d+/.test(n)
        let i = 0
        for (; i < this.courseNumber.length; i++) {
          if (isDigit(this.courseNumber[i])) {
            break
          }
        }
        let keyword = this.courseNumber.slice(0, i).toUpperCase() + ' ' + this.courseNumber.slice(i)
        CoursesService.getPrerequisite(keyword).then((resp) => {
          let course_gpa = eval(resp.data[0]['AvgGpa'])
          let serialized_data = eval(resp.data[0]['Prereq'])
          console.log(course_gpa)
          let course_node = []
          let course_link = []
          let current_course = this.courseNumber.toUpperCase()
          let hid = 0
          serialized_data.map((item, idx) => {
            let source = current_course + (idx === 0 ? '' : '(' + (idx + 1) + ')')
            course_node.push({
              'name': source,
              'x': (idx + 1) * 1000,
              'y': 500,
              'value': course_gpa,
              'itemStyle': {
                color: 'rgb(222, 82, 70)'
              }
            })
            for (let key in item) {
              let node_name = key + (idx === 0 ? '' : '(' + (idx + 1) + ')')
              let node = {
                'name': node_name,
                'x': hid * 700,
                'y': 1600,
                'value': item[key],
                'itemStyle': {
                  color: 'rgb(68, 138, 255)'
                }
              }
              hid += 1
              course_node.push(node)
              course_link.push({source, target: node_name})
            }
          })
          this.polar = {
            tooltip: {
              padding: 10,
              borderWidth: 1,
              formatter: function (node) {
                return 'Avg GPA: ' + node.value.toFixed(2)
              }
            },
            series: [
              {
                type: 'graph',
                symbolSize: 75,
                roam: true,
                label: {
                  show: true,
                  formatter: function (node) {
                    let paren = node.name.indexOf('(')
                    if (paren !== -1) {
                      return node.name.slice(0, paren)
                    }
                    return node.name
                  }
                },
                layout: 'circular',
                edgeSymbol: ['circle', 'arrow'],
                edgeSymbolSize: [4, 10],
                edgeLabel: {
                  fontSize: 20
                },
                data: course_node,
                links: course_link,
                lineStyle: {
                  opacity: 0.9,
                  width: 2,
                },

              }
            ],
            animationDuration: 1000
          }
        })
      },
    }
  }
</script>

<style scoped>
  .wrapper {
    width: 100%;
    height: 600px;
  }

  .echarts {
    width: 100%;
    height: 100%;
  }
</style>
