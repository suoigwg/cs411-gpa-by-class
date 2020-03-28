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
          <option v-for="classNum in classes" :value="classNum" :key="classNum">{{classNum}}</option>
        </select>
      </div>
    </div>
    <div v-if="GPAs.length > 0">
      <div v-if="!editMode">
        <button class="btn btn-primary float-right"
                @click="enterEditMode"
                >
          Edit
        </button>
        <CustomTable :items="GPAs" :itemsPerPage="itemsPerPage" :currentPage="currentPage" @pagechanged="onPageChange"></CustomTable>
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
        <EditableTable :items="tempGPAs" :itemsPerPage="itemsPerPage" :currentPage="currentPage" @pagechanged="onPageChange"></EditableTable>
      </div>
    </div>
  </div>
</template>

<script>
  import CustomTable from '@/components/Table'
  import EditableTable from '@/components/EditableTable'
  import store from '@/store.js'

  export default {
    components: { CustomTable, EditableTable },
    data() {
      return {
        subjects: ['CS'],
        classes: [100, 125],
        selectedSubject: null,
        selectedClass: null,
        editMode: false,
        itemsPerPage: 5,
        currentPage: 1,
        GPAs: [
          { id: 0, subject: 'CS', number: '100', title: 'Intro to CS' },
          { id: 1, subject: 'CS', number: '101', title: 'Intermediate CS' },
          { id: 2, subject: 'CS', number: '102', title: 'Intermediate CS' },
          { id: 3, subject: 'CS', number: '103', title: 'Intermediate CS' },
          { id: 4, subject: 'CS', number: '104', title: 'Intermediate CS' },
          { id: 5, subject: 'CS', number: '105', title: 'Intermediate CS' },
          { id: 6, subject: 'CS', number: '106', title: 'Intermediate CS' },
          { id: 7, subject: 'CS', number: '107', title: 'Intermediate CS' },
          { id: 8, subject: 'CS', number: '108', title: 'Intermediate CS' },
          { id: 9, subject: 'CS', number: '109', title: 'Intermediate CS' },
          { id: 10, subject: 'CS', number: '110', title: 'Intermediate CS' },
          { id: 11, subject: 'CS', number: '111', title: 'Intermediate CS' },
          { id: 12, subject: 'CS', number: '112', title: 'Intermediate CS' },
          { id: 13, subject: 'CS', number: '113', title: 'Intermediate CS' },
          { id: 14, subject: 'CS', number: '114', title: 'Intermediate CS' },
          { id: 15, subject: 'CS', number: '115', title: 'Intermediate CS' },
          { id: 16, subject: 'CS', number: '116', title: 'Intermediate CS' },
          { id: 17, subject: 'CS', number: '117', title: 'Intermediate CS' },
          { id: 18, subject: 'CS', number: '118', title: 'Intermediate CS' },
          { id: 19, subject: 'CS', number: '119', title: 'Intermediate CS' },
        ]
      }
    },
    computed: {
      tempGPAs() {
        return this.GPAs
      }
    },
    methods: {
      loadClassList(event) {
        console.log('Selected: ' + event.target.value)
        // TODO: call class list api
      },

      loadGPAInfo(event) {
        console.log('Selected: ' + event.target.value)
        // TODO
      },

      onPageChange(page) {
        this.currentPage = page
      },

      enterEditMode() {
        this.editMode = true
      },

      saveEdit() {
        this.editMode = false
      },

      cancelEdit() {
        this.editMode = false
        console.log(store.state.deletedItems)
        store.clearEdit()
      }
    }
  }
</script>
