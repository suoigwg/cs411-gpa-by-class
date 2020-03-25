<template>
  <div class="page-container">
    <md-app>
      <md-app-toolbar class="md-primary">
        <span class="md-title">{{page}}</span>
      </md-app-toolbar>
      <md-app-drawer md-permanent="full">
        <md-toolbar class="md-transparent" md-elevation="0">
          Filters
        </md-toolbar>

        <md-list>
          <md-list-item v-on:click="page='All Grades'">
            <md-icon>donut_large</md-icon>
            <span class="md-list-item-text">All Courses</span>
          </md-list-item>

          <md-list-item v-on:click="page='By Course/Instructor'">
            <md-icon>menu_book</md-icon>
            <span class="md-list-item-text">By Course/Instructor</span>
          </md-list-item>

          <md-list-item v-on:click="page='By Department'">
            <md-icon>apartment</md-icon>
            <span class="md-list-item-text">By Department</span>
          </md-list-item>

          <md-list-item>
            <md-icon>compare_arrows</md-icon>
            <span class="md-list-item-text">Prereq</span>
          </md-list-item>

          <md-list-item>
            <md-icon>account_circle</md-icon>
            <span class="md-list-item-text">Update</span>
          </md-list-item>
        </md-list>
      </md-app-drawer>

      <md-app-content>
        <CourseHistory v-if="page==='By Course/Instructor'"></CourseHistory>
        <DepartmentHistory v-if="page==='By Department'"></DepartmentHistory>
        <AllGrades v-if="page==='All Grades'"></AllGrades>
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
        msg: 'Welcome to Your Vue.js App',
        page: 'By Course/Instructor'
      }
    },
    components: {
      // eslint-disable-next-line camelcase
      CourseHistory,
      DepartmentHistory,
      AllGrades
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
    width: 236px;
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
