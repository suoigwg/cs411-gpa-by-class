<template>
  <div class="container page">
    <div class="col-md-6 offset-md-3">
      <h1>Sign in</h1>
      <form @submit.prevent="onSubmit(username, password)">
        <fieldset class="form-group">
          <input class="form-control form-control-lg"
                 type="text"
                 v-model="username"
                 placeholder="Username" />
        </fieldset>
        <fieldset class="form-group">
          <input class="form-control form-control-lg"
                 type="password"
                 v-model="password"
                 placeholder="Password" />
        </fieldset>
        <button class="btn btn-lg btn-primary">
          Sign in
        </button>
      </form>
    </div>
  </div>
</template>

<script>
  import {UserService} from '@/api.service'
  import store from '@/store.js'

  export default {
    name: 'Login',
    data() {
      return {
        username: null,
        password: null
      }
    },
    methods: {
      onSubmit(username, password) {
        UserService.login(username, password).then((data) => {
          store.state.username = data.username
          store.state.isAdmin = data.isAdmin
          store.state.loggedIn = true

          this.$router.push({name: 'home'})
        }).catch((error) => {
          console.log(error)
        })
      }
    }
  }
</script>
