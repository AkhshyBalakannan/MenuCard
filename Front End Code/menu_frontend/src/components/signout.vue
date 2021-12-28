<template>
  <div class="container mt-5 px-5">
    <h1>Successfully signed out !</h1>
    <router-link to="/menucard">Want to sign in again</router-link>
  </div>
</template>

<script>
export default {
  data() {
    return {
    };
  },
  beforeMount() {
    if (this.$store.getters.auth.loggedIn) {
      this.$store.dispatch("troggle_off_auth");
      this.$store.dispatch("troggle_off_admin");
      this.$store.dispatch("delete_token");
    }
  },
};
</script>

<style>
</style>