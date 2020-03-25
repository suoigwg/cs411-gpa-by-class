<template>
  <div>
    <div>
      <md-menu md-direction="bottom-end">
        <md-button md-menu-trigger>Select Department</md-button>
        <md-menu-content>
          <md-menu-item @click="setDepartment">CS</md-menu-item>
          <md-menu-item @click="setDepartment">ECE</md-menu-item>
        </md-menu-content>
      </md-menu>
    </div>
    <BarChart></BarChart>
  </div>
</template>
<script>
  import BarChart from '../bar_chart/BarChart'

  export default {
    data: function () {
      return {
        department: ''
      }
    },
    components: {
      BarChart
    },
    watch: {
      department: function () {

      }
    },
    mounted() {
    },
    methods: {
      setDepartment: function (event) {
        this.department = event.target.innerText
        console.log(this.department)
      }
    }

  }
</script>

<style>
  .small {
    max-width: 1000px;
    margin: 10px auto;
    max-height: 150px;
  }

</style>
