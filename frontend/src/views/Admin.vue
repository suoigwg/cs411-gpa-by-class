<template>
  <div class="container page">
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
  </div>
</template>

<script>
  export default {
    data() {
      return {
        subjects: [],
        classes: [],
        selectedSubject: null,
        selectedClass: null
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
      }
    }
  }
</script>
