<template>
  <div>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
      <div class="container">
        <button
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarTogglerDemo03"
          aria-controls="navbarTogglerDemo03"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span class="navbar-toggler-icon"></span>
        </button>
        <a class="navbar-brand" href="#">ABC-MenuCard</a>
        <div class="collapse navbar-collapse" id="navbarTogglerDemo03">
          <ul class="navbar-nav me-auto mb-2 mb-lg-0">
            <li class="nav-item">
              <router-link to="/">home</router-link>
            </li>
            &nbsp;&nbsp;
            <li class="nav-item">
              <router-link to="/menucard">Check your menu</router-link>
            </li>
            &nbsp;&nbsp;
            <li class="nav-item">
              <router-link to="/food">Food</router-link>
            </li>
            &nbsp;&nbsp;
            <li class="nav-item">
              <router-link to="/profile">Profile</router-link>
            </li>
          </ul>
          <span class="d-flex" v-if="!current_user">
            <button class="btn btn-outline-warning" type="button">
              <router-link to="/signin">sign In</router-link>
            </button>
            <button class="btn btn-outline-warning" type="button">
              <router-link to="/register">sign Up</router-link>
            </button>
          </span>
          <span class="d-flex" v-if="current_user">
            <button class="btn btn-outline-warning" type="button">
              <router-link to="/signout">Sign Out</router-link>
            </button>
          </span>
        </div>
      </div>
    </nav>
  </div>
</template>

<script>
export default {
  props: {
    current_user: {
      type: Boolean,
      required: true,
    },
  },
  data() {
    return {
      msg: "Welcome to Your Vue.js App",
    };
  },
};
</script>

<style>
a {
  text-decoration: none;
  color: white;
}
.router-link-exact-active {
  background-color: white;
  color: black;
}
</style>
