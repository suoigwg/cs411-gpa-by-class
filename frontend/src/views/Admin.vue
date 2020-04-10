<template>
  <div>
    <h3>Admin Page</h3>
    <div>
      <label for="subjectSelect">Subject:</label>
      <select id="subjectSelect" v-model="selectedSubject" @change="loadClassList">
        <option v-for="subject in subjects" :value="subject" :key="subject">{{subject}}</option>
      </select>
      <div v-if="classes.length > 0">
        <label for="classSelect">Number:</label>
        <select id="classSelect" v-model="selectedClass" @change="loadGPAInfo">
          <option v-for="(classNum, index) in classes" :value="classNum" :key="index">{{classNum}}</option>
        </select>
      </div>
    </div>
    <div v-if="items.length > 0">
      <div v-if="!editMode">
        <button class="btn btn-primary float-right"
                @click="enterEditMode"
                >
          Edit
        </button>
        <CustomTable :items="items" :itemsPerPage="itemsPerPage" :currentPage="currentPage" @pagechanged="onPageChange"></CustomTable>
      </div>
      <div v-else>
        <button class="btn btn-danger float-right"
                @click="cancelEdit"
                >
          Cancel
        </button>
        <button class="btn btn-success float-right"
                @click="saveEdit"
                >
          Save
        </button>
        <EditableTable :items="items" :itemsPerPage="itemsPerPage" :currentPage="currentPage" @pagechanged="onPageChange"></EditableTable>
      </div>
    </div>
  </div>
</template>

<script>
  import CustomTable from '@/components/Table'
  import EditableTable from '@/components/EditableTable'
  import store from '@/store.js'
  import { CoursesService, GPAService } from '@/api.service.js'

  export default {
    components: { CustomTable, EditableTable },
    data() {
      return {
        subjects: [],
        classes: [],
        selectedSubject: null,
        selectedClass: null,
        editMode: false,
        itemsPerPage: 5,
        currentPage: 1,
        items: [],
        masterItemList: []
      }
    },
    computed: {
      tempItems() {
        return this.items
      }
    },
    methods: {
      loadClassList() {
        CoursesService.getCourses(this.selectedSubject)
          .then(response => {
            console.log(response)
            this.classes = response.data.map(elem => elem.courseno)
            this.items = response.data
          })
          .catch(error => (console.log(error)))
      },

      loadGPAInfo() {
        GPAService.getGPAInfo(this.selectedSubject + this.selectedClass)
          .then(response => {
            console.log(response)
            this.items = response.data
          })
          .catch(error => (console.log(error)))
      },

      onPageChange(page) {
        this.currentPage = page
      },

      enterEditMode() {
        this.masterItemList = JSON.parse(JSON.stringify(this.items))
        this.editMode = true
      },

      saveEdit() {
        this.editMode = false
        if (this.selectedClass) {
          if (store.state.newItems.length > 0) {
            GPAService.newCourses(store.state.newItems)
              .then(response => {
                console.log(response)
                this.loadGPAInfo()
              })
              .catch(error => (console.log(error)))
          }
          if (store.state.updatedItems.length > 0) {
            GPAService.updateCourses(store.state.updatedItems)
              .then(response => {
                console.log(response)
                this.loadGPAInfo()
              })
              .catch(error => (console.log(error)))
          }
          if (store.state.deletedItems.length > 0) {
            GPAService.deleteCourses(store.state.deletedItems)
              .then(response => {
                console.log(response)
                this.loadGPAInfo()
              })
              .catch(error => (console.log(error)))
          }
        } else {
          if (store.state.newItems.length > 0) {
            CoursesService.newCourses(store.state.newItems)
              .then(response => {
                console.log(response)
                this.loadClassList()
              })
              .catch(error => (console.log(error)))
          }
          if (store.state.updatedItems.length > 0) {
            CoursesService.updateCourses(store.state.updatedItems)
              .then(response => {
                console.log(response)
                this.loadClassList()
              })
              .catch(error => (console.log(error)))
          }
          if (store.state.deletedItems.length > 0) {
            CoursesService.deleteCourses(store.state.deletedItems)
              .then(response => {
                console.log(response)
                this.loadClassList()
              })
              .catch(error => (console.log(error)))
          }
        }
        store.clearEdit()
      },

      cancelEdit() {
        this.editMode = false
        this.items = this.masterItemList
        store.clearEdit()
      }
    },
    created() {
      CoursesService.getSubjects()
        .then(response => {
          console.log(response)
          this.subjects = response.data
        })
        .catch(error => (console.log(error)))
    }
  }
</script>
