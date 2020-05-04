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
      <li class="nav-item" v-if="sharedState.isAdmin">
        <router-link class="nav-link"
                     active-class="active"
                     exact :to="{name: 'admin'}"
                     >
          Admin
        </router-link>
      </li>
    </ul>
    <ul v-if="!sharedState.loggedIn" class="navbar-nav ml-auto">
      <li class="nav-item">
        <router-link class="nav-link"
                     active-class="active"
                     exact :to="{name: 'login'}"
        >
          Login
        </router-link>
      </li>
      <li class="nav-item">
        <router-link class="nav-link"
                     active-class="active"
                     exact :to="{name: 'register'}"
        >
          Register
        </router-link>
      </li>
    </ul>
    <ul v-else class="navbar-nav ml-auto">
      <li class="nav-item">
        <div> Hi {{sharedState.username}}!</div>
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
        sharedState: store.state
      }
    }
  }
</script>
