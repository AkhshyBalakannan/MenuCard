<template>
  <div id="app">
    <router-link to="/signin" />
    <router-link to="/signup" />
   <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: "app",
  data() {
    return {
      msg: "Welcome to Your Vue.js App",
    };
  },
};
</script>

<style>

</style>
