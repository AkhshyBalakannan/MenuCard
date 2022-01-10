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
        <a class="navbar-brand" href="/menucard">ABC-MenuCard</a>
        <div class="collapse navbar-collapse" id="navbarTogglerDemo03">
          <ul class="navbar-nav me-auto mb-2 mb-lg-0">
            <li class="nav-item">
              <router-link to="/menucard">Check your menu</router-link>
            </li>

            <li class="nav-item">
              <router-link to="/food">Food</router-link>
            </li>

            <li class="nav-item" v-if="admin_user">
              <router-link to="/food/edit">-CRUD</router-link>
            </li>

            <li class="nav-item">
              <router-link to="/meal">Meal</router-link>
            </li>

            <li class="nav-item" v-if="admin_user">
              <router-link to="/meal/edit">-CRUD</router-link>
            </li>

            <li class="nav-item" v-if="admin_user">
              <router-link to="/link">Link Meal & Food</router-link>
            </li>

            <li class="nav-item" v-if="admin_user">
              <router-link to="/users/edit">All Users</router-link>
            </li>

            <li class="nav-item">
              <router-link to="/profile">Profile</router-link>
            </li>
          </ul>
          <span class="d-flex" v-if="!current_user">
            <button class="btn btn-outline-warning" type="button">
              <router-link to="/signin">sign In</router-link>
            </button>
            <button class="btn btn-outline-warning" type="button">
              <router-link to="/signup">sign Up</router-link>
            </button>
          </span>
          <span class="d-flex" v-if="current_user">
            <button class="btn btn-warning" type="button">
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
  data() {
    return {
      current_user: this.$store.getters.auth.loggedIn,
      admin_user: this.$store.getters.auth.isAdmin,
    };
  },
};
</script>

<style>
.nav-item a {
  text-decoration: none;
  color: white;
}
.nav-item .router-link-exact-active {
  background-color: white;
  color: black;
  font-weight: 700;
  padding: 3px 5px 3px 5px;
}
.btn a {
  text-decoration: none;

  color: black;
}
.nav-item {
  margin: 0px 10px 0px 10px;
}
</style>
