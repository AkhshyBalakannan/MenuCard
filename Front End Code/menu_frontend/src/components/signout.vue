<template>
  <div class="container">
    <h1>Successfully signed out !</h1>
    <router-link to='/signin'>Want to sign in again</router-link>
  </div>
</template>

<script>
export default {
  data() {
    return {};
  },
  beforeMount() {
    console.log("Removing Token");
    if (this.$cookie.get("token")) {
      this.$cookie.delete("token");
    }
    this.$router.push('/')
  },
};
</script>

<style>
</style>