<template>
  <div>
    <h3>Admin Page</h3>
    <div>
      <label for="subjectSelect">Subject:</label>
      <select id="subjectSelect" v-model="selectedSubject" @change="loadClassList">
        <option v-for="subject in subjects" :value="subject" :key="subject">{{subject}}</option>
      </select>
      <div v-if="classes.length > 0">
        <label for="classSelect">Class:</label>
        <select id="classSelect" v-model="selectedClass" @change="loadGPAInfo">
          <option v-for="classNum in classes" :value="classNum" :key="classNum">{{classNum}}</option>
        </select>
      </div>
    </div>
    <div v-if="GPAs.length > 0">
      <CustomTable :items="GPAs"></CustomTable>
    </div>
  </div>
</template>

<script>
  import CustomTable from '@/components/Table'

  export default {
    components: { CustomTable },
    data() {
      return {
        subjects: [],
        classes: [],
        selectedSubject: null,
        selectedClass: null,
        GPAs: [
          { subject: 'CS', number: '100', title: 'Intro to CS' },
          { subject: 'CS', number: '101', title: 'Intermediate CS' },
          { subject: 'CS', number: '102', title: 'Intermediate CS' },
          { subject: 'CS', number: '103', title: 'Intermediate CS' },
          { subject: 'CS', number: '104', title: 'Intermediate CS' },
          { subject: 'CS', number: '105', title: 'Intermediate CS' },
          { subject: 'CS', number: '106', title: 'Intermediate CS' },
          { subject: 'CS', number: '107', title: 'Intermediate CS' },
          { subject: 'CS', number: '108', title: 'Intermediate CS' },
          { subject: 'CS', number: '109', title: 'Intermediate CS' },
          { subject: 'CS', number: '110', title: 'Intermediate CS' },
          { subject: 'CS', number: '111', title: 'Intermediate CS' },
          { subject: 'CS', number: '112', title: 'Intermediate CS' },
          { subject: 'CS', number: '113', title: 'Intermediate CS' },
          { subject: 'CS', number: '114', title: 'Intermediate CS' },
          { subject: 'CS', number: '115', title: 'Intermediate CS' },
          { subject: 'CS', number: '116', title: 'Intermediate CS' },
          { subject: 'CS', number: '117', title: 'Intermediate CS' },
          { subject: 'CS', number: '118', title: 'Intermediate CS' },
          { subject: 'CS', number: '119', title: 'Intermediate CS' },
        ]
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
    }
  }
</script>
