<template>
  <nav class="navbar navbar-expand-md navbar-light bg-light">
    <ul class="navbar-nav mr-auto">
      <li class="nav-item">
        <router-link class="nav-link"
                     active-class="active"
                     exact
                     :to="{name: 'home'}"
                     >
          GPA History
        </router-link>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="/prereq">Class Prerequistes</a>
      </li>
    </ul>
    <ul v-if="!loggedIn" class="navbar-nav ml-auto">
      <li class="nav-item">
        <router-link class="nav-link"
                     active-class="active"
                     exact :to="{name: 'login'}"
                     >
          Login
        </router-link>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="/register">Register</a>
      </li>
    </ul>
    <ul v-else class="navbar-nav ml-auto">
      <li class="nav-item">
        <div> Hi {{username}}!</div>
      </li>
    </ul>
</nav>
</template>

<script>
import store from '@/store.js'

export default {
  name: 'MyHeader',
  data() {
    return {
      username: store.state.username,
      loggedIn: store.state.loggedIn
    }
  }
}
</script>
