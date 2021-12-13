<template>
  <div>
    <h1>MENUCARD PAGE</h1>
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  data() {
    return {};
  },
  created() {
    console.log(this.$store.getters.auth.loggedIn);
  },
};
</script>

<style>
</style>
