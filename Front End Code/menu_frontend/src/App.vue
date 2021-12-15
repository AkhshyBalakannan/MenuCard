<template>
  <div id="app" :key="$route.fullPath">
    <app-navbar v-show="navbarCheck()"></app-navbar>
    <div class="container">
    <router-view></router-view>

    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {};
  },
  methods: {
    navbarCheck() {
      console.log(this.$route.fullPath);
      if (
        this.$route.fullPath === "/signin" ||
        this.$route.fullPath === "/signup"
      ) {
        return false;
      }
      return true;
    },
  },
};
</script>

<style>
</style>
