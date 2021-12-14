<template>
  <div id="app" :key="$route.fullPath">
    <app-navbar></app-navbar>
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  data() {
    return {};
  },
};
</script>

<style>
</style>
