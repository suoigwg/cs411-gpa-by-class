<template>
  <div class="page-container">
    <md-app>
      <md-app-toolbar class="md-primary">
        <md-button class="md-icon-button" @click="menuVisible = !menuVisible">
          <md-icon>menu</md-icon>
        </md-button>
        <span class="md-title">{{page}}</span>
      </md-app-toolbar>
      <md-app-drawer :md-active.sync="menuVisible">
        <md-toolbar class="md-transparent" md-elevation="0">
          Filters
        </md-toolbar>

        <md-list>
          <md-list-item>
            <md-icon>donut_large</md-icon>
            <span class="md-list-item-text" v-on:click='navigate'>Department Average Grades</span>
          </md-list-item>

          <md-list-item>
            <md-icon>menu_book</md-icon>
            <span class="md-list-item-text" v-on:click='navigate'>By Course</span>
          </md-list-item>

          <md-list-item>
            <md-icon>apartment</md-icon>
            <span class="md-list-item-text" v-on:click='navigate'>By Department</span>
          </md-list-item>

          <md-list-item>
            <md-icon>compare_arrows</md-icon>
            <span class="md-list-item-text">Prereq</span>
          </md-list-item>

        </md-list>
      </md-app-drawer>

      <md-app-content>
        <CourseHistory v-if="page==='By Course'"></CourseHistory>
        <DepartmentHistory v-if="page==='By Department'"></DepartmentHistory>
        <AllGrades v-if="page==='Department Average Grades'"></AllGrades>
      </md-app-content>
    </md-app>
  </div>
</template>
<script>
  // eslint-disable-next-line camelcase
  import CourseHistory from './course_history/CourseHistory'
  import DepartmentHistory from './department/DepartmentHistory'
  import AllGrades from './all_grades/AllGrades'

  export default {
    name: 'HelloWorld',
    data() {
      return {
        page: 'All Grades',
        menuVisible: true,
      }
    },
    components: {
      CourseHistory,
      DepartmentHistory,
      AllGrades
    },
    methods: {
      navigate: function (event) {
        this.page = event.target.innerText
        this.menuVisible = false
      }
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .md-app {
    height: 100vh;
    border: 1px solid rgba(0, 0, 0, .12);
  }

  .md-drawer {
    width: 300px;
    max-width: calc(100vw - 125px);
  }

  h1, h2 {
    font-weight: normal;
  }

  ul {
    list-style-type: none;
    padding: 0;
  }

  li {
    display: inline-block;
    margin: 0 10px;
  }

  a {
    color: #42b983;
  }
</style>
