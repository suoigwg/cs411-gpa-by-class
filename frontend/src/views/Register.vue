<template>
  <div class="container page">
    <div class="col-md-6 offset-md-3">
      <h1>Register</h1>
      <form @submit.prevent="onSubmit(username, password, passwordAgain, isAdmin)">
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
        <fieldset class="form-group">
          <input class="form-control form-control-lg"
                 type="password"
                 v-model="passwordAgain"
                 placeholder="Please type your password again" />
        </fieldset>
        <fieldset class="form-group">
          <input class="form-control"
                 type="checkbox"
                 v-model="isAdmin"
                 name="isAdmin" />
          <label for="isAdmin">Admin User</label>
        </fieldset>
        <button class="btn btn-lg btn-primary">
          Register
        </button>
      </form>
    </div>
  </div>
</template>

<script>
  import { UserService } from '@/api.service'
  import store from '@/store.js'
  export default {
    name: 'Register',
    data() {
      return {
        username: null,
        password: null,
        passwordAgain: null,
        isAdmin: false
      }
    },
    methods: {
      onSubmit(username, password, passwordAgain, isAdmin) {
        if (password === passwordAgain) {
          UserService.register(username, password, isAdmin).then((data) => {
            store.state.username = username
            store.state.isAdmin = isAdmin
            store.state.loggedIn = true

            this.$router.push({ name: 'home' })
          }).catch((error) => {
            console.log(error)
          })
        } else {
          console.log('Passwords do not match')
        }
      }
    }
  }
</script>
